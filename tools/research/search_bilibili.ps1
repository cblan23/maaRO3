param(
    [Parameter(Mandatory = $true)]
    [string]$Query,

    [ValidateRange(1, 5)]
    [int]$Pages = 2,

    [ValidateRange(1, 100)]
    [int]$Limit = 100,

    [switch]$Compact
)

$ErrorActionPreference = 'Stop'
$headers = @{
    'User-Agent' = 'Mozilla/5.0'
    'Referer' = 'https://search.bilibili.com/'
}

$results = for ($page = 1; $page -le $Pages; $page++) {
    $encoded = [uri]::EscapeDataString($Query)
    $uri = "https://api.bilibili.com/x/web-interface/wbi/search/type?search_type=video&keyword=$encoded&page=$page"
    $response = Invoke-RestMethod -Uri $uri -Headers $headers
    if ($response.code -ne 0) {
        throw "Bilibili search API failed: $($response.message)"
    }
    foreach ($item in $response.data.result) {
        [pscustomobject]@{
            Bvid = $item.bvid
            Title = [System.Net.WebUtility]::HtmlDecode(($item.title -replace '<[^>]+>', ''))
            Duration = $item.duration
            Author = $item.author
            PublishedUnix = $item.pubdate
            Plays = $item.play
            Description = $item.description
            Url = "https://www.bilibili.com/video/$($item.bvid)/"
        }
    }
}

$sorted = $results |
    Sort-Object PublishedUnix -Descending |
    Select-Object -First $Limit

if ($Compact) {
    $sorted |
        Select-Object Bvid, Title, Duration, Author, Plays, Url |
        ConvertTo-Json -Depth 4
} else {
    $sorted | Format-Table -Wrap -AutoSize
}
