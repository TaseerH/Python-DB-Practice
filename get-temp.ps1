<#
  .SYNOPSIS
  uberAgent script to determine the current CPU temperature.

  .DESCRIPTION
  Reads the current CPU temperature from WMI and converts the resulting output to the KV format required by uberAgent custom scripts.

  If the default WMI class does not yield satisfactory resulty, try switching to the alternative data source by commenting out the relevant lines.

  Most machines have multiple thermal zones. Test with your PCs and enter the name of the appropriate thermal zone in the variable $thermalZone.
  To retrieve a list of all thermal zones run either of the following:
  - Get-CimInstance -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation
  - Get-CimInstance -ClassName MSAcpi_ThermalZoneTemperature -Namespace "root/wmi"
#>

# Thermal zone (wildcard string)
$thermalZone = "*tz00*"
$thermalZone2 = "*tz01*"
$thermalZone3 = "*tz02*"

# Default: get the CPU temperature from the WMI class Win32_PerfFormattedData_Counters_ThermalZoneInformation
$temp = Get-CimInstance -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation | Where-Object -Property Name -like $thermalZone

$temp1 = Get-CimInstance -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation | Where-Object -Property Name -like $thermalZone2
$temp2 = Get-CimInstance -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation | Where-Object -Property Name -like $thermalZone3

Get-CimInstance -ClassName Win32_PerfFormattedData_Counters_ThermalZoneInformation
$TempKelvin     = $temp.Temperature
$TempKelvin1     = $temp1.Temperature
$TempKelvin2     = $temp2.Temperature

# Alternative: get the CPU temperature from the WMI class MSAcpi_ThermalZoneTemperature
# Note: requires elevation (admin rights)
# $temp = Get-CimInstance -ClassName MSAcpi_ThermalZoneTemperature -Namespace "root/wmi" | Where-Object -Property InstanceName -like $thermalZone
# $TempKelvin     = $temp.Temperature / 10

$TempKelvin     = $temp.Temperature
$TempCelsius    = $TempKelvin - 273.15
$TempFahrenheit = (9/5) * $TempCelsius + 32

$TempKelvin1     = $temp1.Temperature
$TempCelsius1    = $TempKelvin1 - 273.15
$TempFahrenheit1 = (9/5) * $TempCelsius1 + 32

$TempKelvin2     = $temp2.Temperature
$TempCelsius2    = $TempKelvin2 - 273.15
$TempFahrenheit2 = (9/5) * $TempCelsius2 + 32


$Output = @{
   # delete rows which are not needed
   'TempCelsius' = [math]::Round($TempCelsius)
   'TempFahrenheit' = [math]::Round($TempFahrenheit)
   'TempKelvin' = [math]::Round($TempKelvin)
   
   'TempCelsius1' = [math]::Round($TempCelsius1)
   'TempFahrenheit1' = [math]::Round($TempFahrenheit1)
   'TempKelvin1' = [math]::Round($TempKelvin1)
   
   'TempCelsius2' = [math]::Round($TempCelsius2)
   'TempFahrenheit2' = [math]::Round($TempFahrenheit2)
   'TempKelvin2' = [math]::Round($TempKelvin2)
}
Write-Output $($Output.Keys.ForEach({"$_=$($Output.$_)"}) -join ' ')
<#function Get-Temperature {
  $t = Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace "root/wmi"
  $returntemp = @()

  foreach ($temp in $t.CurrentTemperature)
  {


  $currentTempKelvin = $temp / 10
  $currentTempCelsius = $currentTempKelvin - 273.15

  $currentTempFahrenheit = (9/5) * $currentTempCelsius + 32

  $returntemp += $currentTempCelsius.ToString() + " C : " + $currentTempFahrenheit.ToString() + " F : " + $currentTempKelvin + "K"  
  }
  return $returntemp
}

Get-Temperature#>