# SmartHome
SmartHome is a edge computing project applied to smart houses to test and compare performances between edge solution and traditionnal cloud computing solutions.
This was realized for a course at the UQAC (University of Quebec at Chicoutimi) by : Timothée Corsini, Damien LIEHN and Thomas PIOT.

The project is composed of 3 applications :
- The sensors are Python applications that can generate simulated data and send them to a server to be processed. Sensors are also able to turn on/off some of simulated equipment (heat, clim).
- The Edge Server Application is a REST API in C# with ASP.NET Core 3 wich can receive HTTP requests. This application is made to process data received from sensors and to send statistics to the Cloud Server Application when asked.
- The Cloud Server Application is a Python application that can get statistics from the Edge Server Application.


# Setup the applications
## Setup Edge Application ![Edge Workflow](https://github.com/ttgc/SmartHome/workflows/Edge%20Workflow/badge.svg)
The Edge Application is the central one, without this application, all other applications won't work because each of them interact with the edge server.
To setup this application, you should install ASP.NET Core 3, then follow these steps :
1. Run `dotnet restore` to install all dependencies
2. Install PostgreSQL 9 (or above) 
3. Create a postgres database called `edge`
4. Run the SQL script into your new database
5. Copy/Paste the appSettings.json configuration file and rename the copy `appSettings.Production.json`
6. Change the ConnectionString by replacing connection information
7. Run `dotnet publish --configuration Release`
8. Run `dotnet run bin/Release/netcoreapp3.1/Edge.dll`

On Windows you can also run directly the application using Visual Studio (Skipping step 7 and 8). 
Simply open the `.sln` project file, setup the database and run the application.
If done correctly, you should see a web interface (Swagger) to test the API. 
By the way, at step 5 you should rename the file `appSettings.Development.json` if you're running under Visual Studio.

## Setup Cloud Application ![Cloud Workflow](https://github.com/ttgc/SmartHome/workflows/Cloud%20Workflow/badge.svg)
Follow these steps to run Cloud Application :
1. Install PostgreSQL 9 (or above)
2. Create a postgres database called `cloud`
4. Download and install Python 3 (3.6 or above is highly recommended)
5. Run `pip install -r requirements.pip`
6. Run `python main.py` (i.e. run the main.py script)

## Setup Sensors ![Sensors Workflow](https://github.com/ttgc/SmartHome/workflows/Sensors%20Workflow/badge.svg)
Follow these steps to run Sensors :
1. Download and install Python 3 (3.6 or above is highly recommended)
2. Run `pip install -r requirements.pip`
3. Run `python main.py` (i.e. run the main.py script)
