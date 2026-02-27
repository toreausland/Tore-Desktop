$base = (Resolve-Path "C:\Users\mrntau\OneDrive*N*\Skrivebord\Design MAnual\temp_pptx_extract\ppt\slides").Path

Write-Host "=========================================="
Write-Host "  TEXT BOX POSITIONS (EMU -> inches/cm)"
Write-Host "=========================================="

# Focus on common positioning patterns across key slides
for ($i = 1; $i -le 4; $i++) {
    $file = Join-Path $base "slide$i.xml"
    $raw = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

    Write-Host ""
    Write-Host "--- SLIDE $i ---"

    $xfrms = [regex]::Matches($raw, '<a:xfrm>(?:<a:rot[^/]*/>)?<a:off x="(\d+)" y="(\d+)"/><a:ext cx="(\d+)" cy="(\d+)"/></a:xfrm>')
    $count = 0
    foreach ($m in $xfrms) {
        $x = [int64]$m.Groups[1].Value
        $y = [int64]$m.Groups[2].Value
        $cx = [int64]$m.Groups[3].Value
        $cy = [int64]$m.Groups[4].Value
        if ($cx -eq 0 -and $cy -eq 0) { continue }
        $count++

        $xIn = [math]::Round($x / 914400, 2)
        $yIn = [math]::Round($y / 914400, 2)
        $wIn = [math]::Round($cx / 914400, 2)
        $hIn = [math]::Round($cy / 914400, 2)
        $xCm = [math]::Round($x / 360000, 2)
        $yCm = [math]::Round($y / 360000, 2)
        $wCm = [math]::Round($cx / 360000, 2)
        $hCm = [math]::Round($cy / 360000, 2)

        Write-Host "  Element $count : pos(${xIn}in, ${yIn}in) = (${xCm}cm, ${yCm}cm) | size(${wIn}in x ${hIn}in) = (${wCm}cm x ${hCm}cm)"
    }
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  SHAPE FILLS (non-text rectangles)"
Write-Host "=========================================="

for ($i = 1; $i -le 13; $i++) {
    $file = Join-Path $base "slide$i.xml"
    $raw = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

    $shapeFills = [regex]::Matches($raw, '<a:prstGeom prst="([^"]+)".*?</a:prstGeom>.*?<a:solidFill><a:srgbClr val="([A-Fa-f0-9]{6})"', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if ($shapeFills.Count -gt 0) {
        Write-Host "  Slide $i :"
        foreach ($m in $shapeFills) {
            Write-Host "    Shape: $($m.Groups[1].Value)  Fill: #$($m.Groups[2].Value)"
        }
    }
}

Write-Host ""
Write-Host "=========================================="
Write-Host "  DASH STYLES"
Write-Host "=========================================="
for ($i = 1; $i -le 13; $i++) {
    $file = Join-Path $base "slide$i.xml"
    $raw = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    $dashes = [regex]::Matches($raw, 'prstDash val="([^"]+)"')
    foreach ($d in $dashes) {
        Write-Host "  Slide $i : $($d.Groups[1].Value)"
    }
}
