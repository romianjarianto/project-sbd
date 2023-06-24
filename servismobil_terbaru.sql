-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Jun 2023 pada 05.46
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `servismobil`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `customer`
--

CREATE TABLE `customer` (
  `no_ktp` int(5) NOT NULL,
  `nama_customer` varchar(45) NOT NULL,
  `alamat_customer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `customer`
--

INSERT INTO `customer` (`no_ktp`, `nama_customer`, `alamat_customer`) VALUES
(0, 'ssfsfsfsf', 'oefjdbd jb'),
(123, 'pocsnvsvn', 'jalana jlaann'),
(453, 'ebb', 'b db'),
(7954, 'cnsljnvskv', 'jalandakdnkad'),
(8389, 'P', 'PP'),
(9876, 'jajang', 'jalabxsjbxce'),
(19475, 'Timothy', 'Jl. Pengadah 2'),
(33029, 'Jane', 'Jl. Mawar 10'),
(42745, 'Wowiek', 'Jl. Lolipop 02'),
(47574, 'fd', 'bdb'),
(54950, 'Yisuna', 'Jl. Phila 19'),
(74280, 'Kiki', 'Jl. Ngipik 62'),
(101010, 'pilow', 'jalan kipo'),
(555555, 'yyyyy', 'hhhh'),
(998877, 'yuemes', '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `dealer`
--

CREATE TABLE `dealer` (
  `kode_dealer` varchar(20) NOT NULL,
  `nama_dealer` varchar(45) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `dealer`
--

INSERT INTO `dealer` (`kode_dealer`, `nama_dealer`, `alamat`) VALUES
('M1PW', 'Nasmoco_Salatiga', 'Jl. Ahmad Yani 56'),
('M2PW', 'Nasmoco_Karangjati', 'Jl. Ambarawa 21'),
('M3PW', 'Nasmoco_Klaten', 'Jl. Kuningan 79'),
('M4PW', 'Nasmoco_Semarang', 'Jl. Sudirman 45');

-- --------------------------------------------------------

--
-- Struktur dari tabel `layanan_servis`
--

CREATE TABLE `layanan_servis` (
  `id_layanan` int(11) NOT NULL,
  `nama_layanan` varchar(45) NOT NULL,
  `estimasi_biaya` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `layanan_servis`
--

INSERT INTO `layanan_servis` (`id_layanan`, `nama_layanan`, `estimasi_biaya`) VALUES
(1, 'cek_baut', 50000),
(2, 'ganti_oli', 350000),
(3, 'poles_bodi', 250000),
(4, 'poles_kaca', 150000),
(5, 'salon_mobil', 150000),
(6, 'tambah_angin', 20000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `mobil`
--

CREATE TABLE `mobil` (
  `no_rangka` varchar(20) NOT NULL,
  `no_ktp` int(5) NOT NULL,
  `nama_mobil` varchar(20) NOT NULL,
  `jenis_mobil` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `mobil`
--

INSERT INTO `mobil` (`no_rangka`, `no_ktp`, `nama_mobil`, `jenis_mobil`) VALUES
('8888', 0, 'ajja', 'slsls'),
('F1234', 0, 'Ferrari ', 'sport'),
('MDF1213', 0, 'vios', 'sedan'),
('MH024LP', 4274, 'agya', 'lcgc'),
('MH372HF', 74280, 'veloz', 'lmpv'),
('MH4285K', 54950, 'grsupra', 'sedan'),
('MH82BHF', 19475, 'camry', 'sedan'),
('PLT', 0, 'stradale', 'sport'),
('POPO', 0, 'limo', 'sedan'),
('PPP', 8389, 'LLLL', 'OOOO'),
('PPT', 0, 'super', 'suv'),
('TTTTT', 0, 'ioniq6', 'listrik');

-- --------------------------------------------------------

--
-- Struktur dari tabel `mobil_has_layanan`
--

CREATE TABLE `mobil_has_layanan` (
  `no_rangka` varchar(20) NOT NULL,
  `kode_layanan` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `mobil_has_layanan`
--

INSERT INTO `mobil_has_layanan` (`no_rangka`, `kode_layanan`) VALUES
('MH82BHF', 'JPL1'),
('MH4285K', 'JQT7'),
('MH024LP', 'JPL2'),
('MH372HF', 'JPL1');

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `no_transaksi` int(11) NOT NULL,
  `no_ktp` int(11) NOT NULL,
  `id_layanan` int(11) NOT NULL,
  `tanggal` datetime NOT NULL,
  `total_biaya` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`no_transaksi`, `no_ktp`, `id_layanan`, `tanggal`, `total_biaya`) VALUES
(1, 0, 1, '2023-06-24 01:18:07', 50000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`no_ktp`);

--
-- Indeks untuk tabel `dealer`
--
ALTER TABLE `dealer`
  ADD PRIMARY KEY (`kode_dealer`);

--
-- Indeks untuk tabel `layanan_servis`
--
ALTER TABLE `layanan_servis`
  ADD PRIMARY KEY (`id_layanan`);

--
-- Indeks untuk tabel `mobil`
--
ALTER TABLE `mobil`
  ADD PRIMARY KEY (`no_rangka`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`no_transaksi`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `no_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
