param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^BV[0-9A-Za-z]{10}$')]
    [string]$Bvid,

    [string]$OutputRoot = (Join-Path $env:TEMP 'maaRO3-research'),

    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$headers = @{
    'User-Agent' = 'Mozilla/5.0'
    'Referer' = "https://www.bilibili.com/video/$Bvid/"
    'Origin' = 'https://www.bilibili.com'
    'Accept' = '*/*'
}

function Save-FirstAvailableStream {
    param(
        [Parameter(Mandatory = $true)]
        $Stream,

        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    $candidates = @(
        $Stream.baseUrl
        $Stream.base_url
        $Stream.backupUrl
        $Stream.backup_url
    ) | Where-Object { $_ } | Select-Object -Unique

    $errors = @()
    foreach ($candidate in $candidates) {
        $partial = "$Path.part"
        try {
            if (Test-Path $partial) {
                Remove-Item -LiteralPath $partial -Force
            }
            Invoke-WebRequest -Uri $candidate -Headers $headers -OutFile $partial
            if ((Get-Item -LiteralPath $partial).Length -le 0) {
                throw 'Downloaded stream is empty.'
            }
            Move-Item -LiteralPath $partial -Destination $Path -Force
            return
        } catch {
            $errors += "[$([uri]$candidate).Host] $($_.Exception.Message)"
            if (Test-Path $partial) {
                Remove-Item -LiteralPath $partial -Force
            }
        }
    }

    throw "All stream URLs failed:`n$($errors -join "`n")"
}

$output = Join-Path $OutputRoot $Bvid
New-Item -ItemType Directory -Force -Path $output | Out-Null

$view = Invoke-RestMethod `
    -Uri "https://api.bilibili.com/x/web-interface/view?bvid=$Bvid" `
    -Headers $headers

if ($view.code -ne 0) {
    throw "Bilibili view API failed: $($view.message)"
}

$cid = $view.data.cid
$play = Invoke-RestMethod `
    -Uri "https://api.bilibili.com/x/player/playurl?bvid=$Bvid&cid=$cid&qn=64&fnval=16" `
    -Headers $headers

if ($play.code -ne 0 -or -not $play.data.dash) {
    throw "Bilibili play API failed or returned no DASH streams: $($play.message)"
}

$metadataPath = Join-Path $output 'metadata.json'
$videoPath = Join-Path $output 'video.m4s'
$audioPath = Join-Path $output 'audio.m4s'

$view.data | ConvertTo-Json -Depth 20 | Set-Content -Encoding utf8 $metadataPath

$video = $play.data.dash.video |
    Sort-Object -Property @{ Expression = 'height'; Descending = $true }, @{ Expression = 'bandwidth'; Descending = $true } |
    Select-Object -First 1
$audio = $play.data.dash.audio |
    Sort-Object -Property bandwidth -Descending |
    Select-Object -First 1

if ($Force -or -not (Test-Path $videoPath) -or (Get-Item -LiteralPath $videoPath).Length -le 0) {
    Save-FirstAvailableStream -Stream $video -Path $videoPath
}
if ($Force -or -not (Test-Path $audioPath) -or (Get-Item -LiteralPath $audioPath).Length -le 0) {
    Save-FirstAvailableStream -Stream $audio -Path $audioPath
}

[pscustomobject]@{
    Bvid = $Bvid
    Title = $view.data.title
    DurationSeconds = $view.data.duration
    Metadata = $metadataPath
    Video = $videoPath
    Audio = $audioPath
}
