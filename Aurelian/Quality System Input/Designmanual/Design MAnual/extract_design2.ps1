$base = "C:\Users\mrntau\OneDrive - Mosseregionens Næringsutvikling AS\Skrivebord\Design MAnual\temp_pptx_extract\ppt\slides"

# Debug: check if files exist and have content
$testFile = Join-Path $base "slide1.xml"
Write-Host "File exists: $(Test-Path $testFile)"
$raw = [System.IO.File]::ReadAllText($testFile)
Write-Host "File length: $($raw.Length)"
Write-Host "First 200 chars: $($raw.Substring(0, [Math]::Min(200, $raw.Length)))"

# Test regex
$colorMatches = [regex]::Matches($raw, 'srgbClr val="([A-Fa-f0-9]{6})"')
Write-Host "Color matches count: $($colorMatches.Count)"
foreach ($m in $colorMatches) {
    Write-Host "  Color: $($m.Groups[1].Value)"
}
