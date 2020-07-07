CREATE TABLE public.Temperature(
	timer		    TIMESTAMP WITH TIME ZONE ,
	val					FLOAT CONSTRAINT temperature_val_notnull NOT NULL ,
	heat_on     BOOLEAN ,
	clim_on			BOOLEAN ,
	CONSTRAINT prk_constraint_temperature PRIMARY KEY (timer)
)WITHOUT OIDS;

CREATE TABLE public.StatTemperature(
	statyear 			 CHAR(4) ,
	clim_duration	 INTERVAL CONSTRAINT stattemp_climduration_notnull NOT NULL ,
	heat_duration  INTERVAL CONSTRAINT stattemp_heatduration_notnul NOT NULL ,
	average				 FLOAT CONSTRAINT stattemp_avg_notnull NOT NULL ,
	std_deviation  FLOAT CONSTRAINT stattemp_stddev_notnull NOT NULL ,
	CONSTRAINT prk_constraint_statstemperature PRIMARY KEY (statyear)
)WITHOUT OIDS;

CREATE TABLE public.Settings(
	house_name  VARCHAR(25) ,
	clim_on			FLOAT ,
	clim_off		FLOAT ,
	heat_on     FLOAT ,
	heat_off    FLOAT ,
	temp_unit   CHAR(1) ,
	CONSTRAINT prk_constraint_settings PRIMARY KEY (house_name)
)WITHOUT OIDS;

CREATE TABLE public.UnitsTemperature(
	code  CHAR(1) ,
	nom		VARCHAR(25) ,
	CONSTRAINT prk_constraint_UnitsTemperature PRIMARY KEY (code)
)WITHOUT OIDS;

ALTER TABLE public.settings ADD CONSTRAINT FK_tempunit_unitstempcode FOREIGN KEY (temp_unit) REFERENCES public.UnitsTemperature(code);

INSERT INTO UnitsTemperature VALUES ('C', 'Celsius'), ('F', 'Fahrenheit');
INSERT INTO Settings VALUES ('SmartHome', 30.0, 23.0, 15.0, 20.0, 'C');
