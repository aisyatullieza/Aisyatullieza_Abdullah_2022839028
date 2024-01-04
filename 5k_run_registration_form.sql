-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 02:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5k_run_registration_form`
--

-- --------------------------------------------------------

--
-- Table structure for table `5k_run`
--

CREATE TABLE `5k_run` (
  `participant_full_name` varchar(30) NOT NULL,
  `participant_email` varchar(30) NOT NULL,
  `participant_phone_no` int(10) NOT NULL,
  `participant_age` int(3) NOT NULL,
  `participant_gender` varchar(7) NOT NULL,
  `registration_fee` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `5k_run`
--

INSERT INTO `5k_run` (`participant_full_name`, `participant_email`, `participant_phone_no`, `participant_age`, `participant_gender`, `registration_fee`) VALUES
('MAIMUNAH BT MARKUF', 'maimunahmarkuf@gmail.com', 135678943, 55, 'Female', 21.25),
('NURUL SHARIFAH BT ZALI', 'nurulsharifahzali@gmail.com', 197658433, 12, 'Female', 22.5),
('AIMAN FARIS BIN SHAHRUL', 'aimanfaris@gmail.com', 124577859, 26, 'Male', 25),
('THARIQ RIDZUAN BIN RUIZ', 'thariqridzuanruiz@gmail.com', 184533876, 19, 'Male', 25),
('DINA BATRISYIA MOHD ZAIDI', 'dinabatrisyiazaidi@gmail.com', 113579534, 14, 'Female', 22.5),
('NATASHABILLA BT ABDULLAH', 'natashabilla@gmail.com', 137644987, 65, 'Female', 21.25),
('ABDULLAH BIN SHARIF', 'abdullahsharif@gmail.com', 133295462, 35, 'Male', 25);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
