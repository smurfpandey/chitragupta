
function OnGameStarted()
{
    param(
        $game
    )
   
    $__logger.Info("OnGameStarted $game")

    # Authentication
    $webclient = New-Object System.Net.WebClient

    # Data prep
    $data = @{game=$game.Game; activity="start";} | ConvertTo-Json

    Invoke-RestMethod -Uri "https://chitragupta.home.smurfpandey.me/api/games" -Method Post -ContentType "application/json" -Body $data
    
}

function OnGameStopped()
{
    param($eventArgs)
    $__logger.Info("OnGameStopped $eventArgs")

    # Authentication
    $webclient = New-Object System.Net.WebClient

    # Data prep
    $data = @{game=$eventArgs.Game; activity="stop"; elapsed_seconds=$eventArgs.ElapsedSeconds;} | ConvertTo-Json
    
    Invoke-RestMethod -Uri "https://chitragupta.home.smurfpandey.me/api/games" -Method Post -ContentType "application/json" -Body $data
}
