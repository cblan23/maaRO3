param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9A-Za-z_-]{11}$')]
    [string]$VideoId,

    [string]$OutputRoot = (Join-Path $env:TEMP 'maaRO3-research'),

    [switch]$SavePlayerResponse,

    [switch]$FetchPublicCaptions
)

$ErrorActionPreference = 'Stop'
$output = Join-Path $OutputRoot "YT-$VideoId"
$arguments = @(
    'tools/research/fetch_youtube_watch.py',
    '--video-id', $VideoId,
    '--output', $output
)
if ($SavePlayerResponse) {
    $arguments += '--save-player-response'
}
if ($FetchPublicCaptions) {
    $arguments += '--fetch-public-captions'
}

$env:UV_CACHE_DIR = Join-Path $env:TEMP 'uv-cache'
uv run --python 3.12 python @arguments
if ($LASTEXITCODE -ne 0) {
    throw "YouTube watch-page research fetch failed with exit code $LASTEXITCODE"
}
