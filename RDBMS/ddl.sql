CREATE DATABASE `Grafana`

-- Grafana.UC04_Account_Details definition

CREATE TABLE `UC04_Account_Details` (
  `Account_ID` text DEFAULT NULL,
  `Customer_ID` text DEFAULT NULL,
  `KTP_ID` text DEFAULT NULL,
  `Full_Name` text DEFAULT NULL,
  `Date_of_Birth` text DEFAULT NULL,
  `Gender` text DEFAULT NULL,
  `Email_Address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Grafana.UC04_Results definition

CREATE TABLE `UC04_Results` (
  `Account_Sender` text NOT NULL,
  `Account_Receiver` text NOT NULL,
  `ATM_Trx_ID` text DEFAULT NULL,
  `ATM_Trx_Datetime` text DEFAULT NULL,
  `ATM_Trx_Amount` int(11) DEFAULT NULL,
  `Mobile_Trx_ID` text DEFAULT NULL,
  `Mobile_Trx_Datetime` text DEFAULT NULL,
  `Mobile_Trx_Amount` int(11) DEFAULT NULL,
  `IBank_Trx_ID` text DEFAULT NULL,
  `IBank_Trx_Datetime` text DEFAULT NULL,
  `IBank_Trx_Amount` int(11) DEFAULT NULL,
  `Total_Transaction` int(11) DEFAULT NULL,
  `Anomaly_Datetime` varchar(50) NOT NULL DEFAULT '',
  `Use_Case` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Grafana.UC6a definition

CREATE TABLE `UC6a` (
  `Credit_Card_Trx_ID` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Code` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Type` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Amount` int(11) DEFAULT NULL,
  `Amount` int(11) DEFAULT NULL,
  `Account_Credit_Card_ID` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Datetime` varchar(50) DEFAULT NULL,
  `EDC_Name` varchar(50) DEFAULT NULL,
  `EDC_City` varchar(50) DEFAULT NULL,
  `EDC_Address` varchar(50) DEFAULT NULL,
  `User_Name` varchar(50) DEFAULT NULL,
  `User_Address` varchar(50) DEFAULT NULL,
  `User_Gender` varchar(50) DEFAULT NULL,
  `User_BirthDate` varchar(50) DEFAULT NULL,
  `User_KTP_ID` varchar(50) DEFAULT NULL,
  `Anomaly_timestamp` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Grafana.UC6b definition

CREATE TABLE `UC6b` (
  `Credit_Card_Trx_ID` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Code` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Type` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Amount` int(50) DEFAULT NULL,
  `Account_Credit_Card_ID` varchar(50) DEFAULT NULL,
  `Credit_Card_Trx_Datetime` varchar(50) DEFAULT NULL,
  `EDC_Name` varchar(50) DEFAULT NULL,
  `EDC_City` varchar(50) DEFAULT NULL,
  `EDC_Address` varchar(50) DEFAULT NULL,
  `EDC_Operation_Time_Start` varchar(50) DEFAULT NULL,
  `EDC_Operation_Time_End` varchar(50) DEFAULT NULL,
  `User_Name` varchar(50) DEFAULT NULL,
  `User_Address` varchar(50) DEFAULT NULL,
  `User_Gender` varchar(50) DEFAULT NULL,
  `User_BirthDate` varchar(50) DEFAULT NULL,
  `User_KTP_ID` varchar(50) DEFAULT NULL,
  `Anomaly_timestamp` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Grafana.UC9 definition

CREATE TABLE `UC9` (
  `Rekening_ID` varchar(50) DEFAULT NULL,
  `Total_Transaksi` int(11) DEFAULT NULL,
  `ATM_Area_Location` varchar(50) DEFAULT NULL,
  `ATM_City` varchar(50) DEFAULT NULL,
  `ATM_Latitude` float DEFAULT NULL,
  `ATM_Longitude` float DEFAULT NULL,
  `ATM_Trx_Date` varchar(50) DEFAULT NULL,
  `ATM_Trx_Amount` int(11) DEFAULT NULL,
  `Ibank_Area_Location` varchar(50) DEFAULT NULL,
  `Ibank_Device` varchar(50) DEFAULT NULL,
  `Ibank_Latitude` float DEFAULT NULL,
  `Ibank_Longitude` float DEFAULT NULL,
  `Ibank_Provider` varchar(50) DEFAULT NULL,
  `Ibank_Trx_Date` varchar(50) DEFAULT NULL,
  `Ibank_Trx_Amount` int(11) DEFAULT NULL,
  `Mobile_App_Area_Location` varchar(50) DEFAULT NULL,
  `Mobile_App_City` varchar(50) DEFAULT NULL,
  `Mobile_App_Latitude` float DEFAULT NULL,
  `Mobile_App_Longitude` float DEFAULT NULL,
  `Mobile_App_Provider` varchar(50) DEFAULT NULL,
  `Mobile_App_Trx_Date` varchar(50) DEFAULT NULL,
  `Mobile_App_Device` varchar(50) DEFAULT NULL,
  `Mobile_App_Trx_Amount` int(11) DEFAULT NULL,
  `Customer_ID` varchar(50) DEFAULT NULL,
  `User_Address` varchar(50) DEFAULT NULL,
  `User_BirthDate` varchar(50) DEFAULT NULL,
  `User_Gender` varchar(50) DEFAULT NULL,
  `User_KTP_ID` varchar(50) DEFAULT NULL,
  `User_Name` varchar(50) DEFAULT NULL,
  `Use_Case` varchar(50) DEFAULT NULL,
  `Anomaly_timestamp` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
