CREATE TABLE ATM_Machine (
	ATM_Machine_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	ATM_Brand VARCHAR (50),
	ATM_Type VARCHAR (25),
	ATM_Operation_Code VARCHAR (50),
	ATM_Operation_Time VARCHAR (50),
	ATM_Operation_Time_Start VARCHAR (50),
	ATM_Operation_Time_End VARCHAR (50),
	ATM_Name VARCHAR (50),
	ATM_Latitude FLOAT,
	ATM_Longitude FLOAT,
	ATM_City VARCHAR (50),
	ATM_Area VARCHAR (50),
	ATM_Address VARCHAR (200),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Mobile_Telco (
	Mobile_Telco_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	Mobile_Telco_Name VARCHAR (25),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE Mobile_Device (
	Mobile_Device_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	Mobile_Telco_ID VARCHAR (50) NOT NULL REFERENCES Mobile_Telco (Mobile_Telco_ID),
	Mobile_Device_Brand VARCHAR (50),
	Mobile_Device_OS_Type VARCHAR (20),
	Mobile_Device_OS_Version VARCHAR (5),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Mobile_Trx_Location (
	Mobile_Trx_Location_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	Mobile_Device_ID VARCHAR (50) NOT NULL REFERENCES Mobile_Device (Mobile_Device_ID),
	Mobile_GPS_Latitude FLOAT,
	Mobile_GPS_Longitude FLOAT,
	Mobile_GPS_City VARCHAR (50),
	Mobile_GPS_Area VARCHAR (50),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IBank_Device (
	IBank_Device_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	IBank_Device_Type VARCHAR (20),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IBank_Trx_Location (
	IBank_IP_Address VARCHAR(50) NOT NULL PRIMARY KEY,
	IBank_Device_ID VARCHAR (50) NOT NULL REFERENCES IBank_Device (IBank_Device_ID),
	IBank_Inet_Location VARCHAR (50),
	IBank_IP_Address_Range1 VARCHAR (50),
	IBank_IP_Address_Range2 VARCHAR (50),
	IBank_Inet_Provider VARCHAR (25),
	IBank_Inet_Latitude FLOAT,
	IBank_Inet_Longitude FLOAT,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Transactional_Data (
	Account_Debit_BSI_ID VARCHAR(50) NOT NULL PRIMARY KEY,
	ATM_Card_ID VARCHAR (50) NOT NULL,
	ATM_Machine_ID VARCHAR (50) NOT NULL REFERENCES ATM_Machine (ATM_Machine_ID),
	ATM_Trx_ID VARCHAR (50) UNIQUE NOT NULL,
	ATM_Trx_Code INT NOT NULL,
	ATM_Trx_Type VARCHAR (100),
	ATM_Trx_Amount INT,
	ATM_Trx_Datetime TIMESTAMP NOT NULL,
	Account_Debit_BSI_ID_ATM_Receiver VARCHAR(50),
	Mobile_App_ID VARCHAR (50) NOT NULL,
	Mobile_Location_ID VARCHAR (50) NOT NULL REFERENCES Mobile_Trx_Location (Mobile_Trx_Location_ID),
	Mobile_App_Trx_ID VARCHAR (50) UNIQUE NOT NULL,
	Mobile_App_Trx_Code INT NOT NULL,
	Mobile_App_Trx_Type VARCHAR (100),
	Mobile_App_Trx_Amount INT,
	Mobile_App_Trx_Datetime TIMESTAMP NOT NULL,
	Account_Debit_BSI_ID_Mobile_Receiver VARCHAR(50),
	IBank_ID VARCHAR (50) NOT NULL,
	IBank_IP_Address VARCHAR (50) NOT NULL REFERENCES IBank_Trx_Location (IBank_IP_Address),
	IBank_Trx_ID VARCHAR (50) UNIQUE NOT NULL,
	IBank_Trx_Code INT NOT NULL,
	IBank_Trx_Type VARCHAR (100),
	IBank_Trx_Amount INT,
	IBank_Trx_Datetime TIMESTAMP NOT NULL,
	Account_Debit_BSI_ID_IBank_Receiver VARCHAR(50),
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
