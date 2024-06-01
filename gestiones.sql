-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 01-06-2024 a las 17:49:40
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestiones`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `Condominios_no` int(100) NOT NULL,
  `residente` varchar(250) NOT NULL,
  `valor` varchar(250) NOT NULL,
  `deuda` varchar(250) NOT NULL,
  `infraccion` varchar(250) NOT NULL,
  `desalojo` varchar(250) NOT NULL,
  `motivo` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `curso`
--

INSERT INTO `curso` (`Condominios_no`, `residente`, `valor`, `deuda`, `infraccion`, `desalojo`, `motivo`) VALUES
(1, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(2, 'arturo ', '80$', '50$', 'Aprobada', 'Si', 'incumplimiento de normas'),
(3, 'tilin', '90$', '20$', 'Denegada', 'No', 'Deudor'),
(4, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(5, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(6, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(7, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(8, 'jose torres', '50$', '40$', 'Aprobada', 'Si', 'Deuda'),
(9, 'manuel', '60$', '30$', 'Denegada', 'No', 'Deudor');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`Condominios_no`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `curso`
--
ALTER TABLE `curso`
  MODIFY `Condominios_no` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
