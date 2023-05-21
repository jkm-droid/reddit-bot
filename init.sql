-- MySQL dump 10.17  Distrib 10.3.23-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: bot_admin
-- ------------------------------------------------------
-- Server version	10.3.23-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admins` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `profile_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'blank.profile.picture.png',
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admins_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'jkmdroid','jkmdroid@info.com',NULL,'$2y$10$vyW7zJcaOYw3esJSByqH3ezSVkzrw5aTyzI2m9qWtXx6HA.vviGUS','blank.profile.picture.png',NULL,'2023-04-25 15:40:50','2023-04-25 15:40:50');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bots`
--

DROP TABLE IF EXISTS `bots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bots` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `bot_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `is_initialized` tinyint(1) NOT NULL DEFAULT 0,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bots`
--

LOCK TABLES `bots` WRITE;
/*!40000 ALTER TABLE `bots` DISABLE KEYS */;
INSERT INTO `bots` VALUES (12,2,'travel-bot',1,'2023-05-05 14:27:46','2023-05-05 14:27:46',1,'reddit');
/*!40000 ALTER TABLE `bots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `comment_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_replied` tinyint(1) NOT NULL DEFAULT 0,
  `is_upvoted` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `processing_status` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `response_description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=461 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `failed_jobs`
--

DROP TABLE IF EXISTS `failed_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `failed_jobs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `failed_jobs_uuid_unique` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `failed_jobs`
--

LOCK TABLES `failed_jobs` WRITE;
/*!40000 ALTER TABLE `failed_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `failed_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hashtags`
--

DROP TABLE IF EXISTS `hashtags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hashtags` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hashtags`
--

LOCK TABLES `hashtags` WRITE;
/*!40000 ALTER TABLE `hashtags` DISABLE KEYS */;
INSERT INTO `hashtags` VALUES (1,3,'corrupti','2023-04-24 15:51:52','2023-04-24 15:51:52'),(2,5,'omnis','2023-04-24 15:51:52','2023-04-24 15:51:52'),(3,6,'cum','2023-04-24 15:51:52','2023-04-24 15:51:52'),(4,4,'mollitia','2023-04-24 15:51:52','2023-04-24 15:51:52'),(5,1,'dolorem','2023-04-24 15:51:52','2023-04-24 15:51:52'),(6,1,'aut','2023-04-24 15:51:52','2023-04-24 15:51:52'),(7,8,'nihil','2023-04-24 15:51:53','2023-04-24 15:51:53'),(8,2,'eum','2023-04-24 15:51:53','2023-04-24 15:51:53'),(9,5,'laudantium','2023-04-24 15:51:53','2023-04-24 15:51:53'),(10,1,'odit','2023-04-24 15:51:53','2023-04-24 15:51:53'),(11,6,'cumque','2023-04-24 15:51:53','2023-04-24 15:51:53'),(12,9,'quibusdam','2023-04-24 15:51:53','2023-04-24 15:51:53'),(13,5,'est','2023-04-24 15:51:53','2023-04-24 15:51:53'),(14,10,'atque','2023-04-24 15:51:53','2023-04-24 15:51:53'),(15,8,'est','2023-04-24 15:51:53','2023-04-24 15:51:53'),(16,6,'ex','2023-04-24 15:51:53','2023-04-24 15:51:53'),(17,8,'neque','2023-04-24 15:51:53','2023-04-24 15:51:53'),(18,1,'autem','2023-04-24 15:51:53','2023-04-24 15:51:53'),(19,7,'dolorem','2023-04-24 15:51:53','2023-04-24 15:51:53'),(20,1,'fugiat','2023-04-24 15:51:53','2023-04-24 15:51:53'),(21,3,'odio','2023-04-24 15:51:53','2023-04-24 15:51:53'),(22,9,'natus','2023-04-24 15:51:53','2023-04-24 15:51:53'),(23,6,'molestias','2023-04-24 15:51:53','2023-04-24 15:51:53'),(24,9,'illum','2023-04-24 15:51:53','2023-04-24 15:51:53'),(25,5,'ducimus','2023-04-24 15:51:53','2023-04-24 15:51:53'),(26,8,'laudantium','2023-04-24 15:51:53','2023-04-24 15:51:53'),(27,7,'optio','2023-04-24 15:51:54','2023-04-24 15:51:54'),(28,2,'qui','2023-04-24 15:51:54','2023-04-24 15:51:54'),(29,9,'sequi','2023-04-24 15:51:54','2023-04-24 15:51:54'),(30,9,'est','2023-04-24 15:51:54','2023-04-24 15:51:54'),(31,3,'molestiae','2023-04-24 15:51:54','2023-04-24 15:51:54');
/*!40000 ALTER TABLE `hashtags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `headings`
--

DROP TABLE IF EXISTS `headings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `headings` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `headings`
--

LOCK TABLES `headings` WRITE;
/*!40000 ALTER TABLE `headings` DISABLE KEYS */;
INSERT INTO `headings` VALUES (1,8,'Need help with your homework? DM us.','2023-04-24 15:51:56','2023-04-24 15:51:56'),(2,9,'We will do your assignments at reasonable rates.','2023-04-24 15:51:56','2023-04-24 15:51:56'),(3,8,'Customer satisfaction is our ultimate priority.','2023-04-24 15:51:56','2023-04-24 15:51:56'),(4,1,'Hire our professionals to ace your assignments.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(5,5,'Struggling with your assignment(s)?','2023-04-24 15:51:57','2023-04-24 15:51:57'),(6,8,'Look no more for legit and affordable writers.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(7,3,'Securing you top grades is our top priority.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(8,5,'Struggling with your homework?','2023-04-24 15:51:57','2023-04-24 15:51:57'),(9,1,'Need help with your assignments?','2023-04-24 15:51:57','2023-04-24 15:51:57'),(10,5,'Dm us for quality case study at a fair cost.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(11,8,'DM us for help in your homework.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(12,10,'Pay us to do your assignment(s)','2023-04-24 15:51:57','2023-04-24 15:51:57'),(13,7,'DM for help in your assignments(s).','2023-04-24 15:51:57','2023-04-24 15:51:57'),(14,4,'Pay us to write your essay(s).','2023-04-24 15:51:57','2023-04-24 15:51:57'),(15,8,'Pay us to write your assignments(s).','2023-04-24 15:51:57','2023-04-24 15:51:57'),(16,8,'100% help in your assignment.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(17,2,'100% assurance help in academic writing.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(18,7,'Hire us for academic writing.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(19,5,'Plagiarism free papers.','2023-04-24 15:51:57','2023-04-24 15:51:57'),(20,4,'Need help with an essay?','2023-04-24 15:51:58','2023-04-24 15:51:58'),(21,3,'We\'re a legit writing team.','2023-04-24 15:51:58','2023-04-24 15:51:58'),(22,1,'A+ assurance in your essay(s).','2023-04-24 15:51:58','2023-04-24 15:51:58'),(23,7,'A+ assured in your assignment(s).','2023-04-24 15:51:58','2023-04-24 15:51:58'),(24,4,'A+ assured in your academic work.','2023-04-24 15:51:58','2023-04-24 15:51:58'),(25,5,'Do you have assignments bothering you!','2023-04-24 15:51:58','2023-04-24 15:51:58'),(26,9,'We work hard to deliver that desired Grade A+.','2023-04-24 15:51:58','2023-04-24 15:51:58'),(27,3,'Kindly consider our services at an affordable fee.','2023-04-24 15:51:58','2023-04-24 15:51:58'),(28,3,'Get help from a professional team.','2023-04-24 15:51:58','2023-04-24 15:51:58'),(29,9,'Need a hand in your due assignments?','2023-04-24 15:51:59','2023-04-24 15:51:59');
/*!40000 ALTER TABLE `headings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keywords`
--

DROP TABLE IF EXISTS `keywords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keywords` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_extracted` tinyint(1) NOT NULL DEFAULT 0,
  `is_locked` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keywords`
--

LOCK TABLES `keywords` WRITE;
/*!40000 ALTER TABLE `keywords` DISABLE KEYS */;
INSERT INTO `keywords` VALUES (30,12,'Kenya safari','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 19:53:00'),(31,12,'Maasai Mara','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 19:58:00'),(32,12,'Amboseli National Park','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:05:00'),(33,12,'Tsavo East and West','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:10:00'),(34,12,'Samburu National Reserve','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:16:00'),(35,12,'Great Migration','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:21:00'),(36,12,'Big Five','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:27:00'),(37,12,'Game drive','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:32:00'),(38,12,'Wildlife spotting','reddit',1,0,'2023-05-05 14:29:30','2023-05-20 20:37:00'),(39,12,'Safari camps and lodges','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 20:43:00'),(40,12,'Hot air balloon safari','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 20:49:00'),(41,12,'Birdwatching','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 20:55:00'),(42,12,'Nairobi National Park','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:01:00'),(43,12,'Lake Nakuru National Park','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:07:00'),(44,12,'Ol Pejeta Conservancy','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:13:00'),(45,12,'Guided bush walks','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:19:00'),(46,12,'Laikipia Plateau','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:24:00'),(47,12,'Rift Valley','reddit',1,0,'2023-05-05 14:29:31','2023-05-20 21:30:00'),(48,12,'Aberdare National Park','reddit',0,0,'2023-05-05 14:29:31','2023-05-20 19:42:00'),(49,12,'Safari photography','reddit',0,0,'2023-05-05 14:29:32','2023-05-20 19:47:00');
/*!40000 ALTER TABLE `keywords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrations` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
INSERT INTO `migrations` VALUES (16,'2014_10_12_000000_create_users_table',1),(17,'2014_10_12_100000_create_password_resets_table',1),(18,'2019_08_19_000000_create_failed_jobs_table',1),(19,'2019_12_14_000001_create_personal_access_tokens_table',1),(20,'2023_04_23_085423_create_bots_table',1),(22,'2023_04_23_085610_create_subjects_table',1),(23,'2023_04_23_085619_create_hashtags_table',1),(24,'2023_04_23_085647_create_headings_table',1),(25,'2023_04_23_085659_create_slogans_table',1),(26,'2023_04_23_085716_create_universities_table',1),(27,'2023_04_23_134821_add_is_initialized_field_to_bots_table',1),(28,'2023_04_24_181816_add_type_field_to_bots_table',1),(29,'2023_04_24_182130_add_type_field_to_keywords_table',1),(30,'2023_04_24_182706_create_admins_table',1),(31,'2023_05_01_072520_create_sub_reddits_table',2),(32,'2023_05_01_073101_create_comments_table',2),(33,'2023_05_01_073111_create_submissions_table',2),(34,'2023_05_01_091657_create_reddit_replies_table',3),(35,'2023_04_23_085435_create_keywords_table',4),(36,'2023_05_13_181743_add_content_field_to_submissions_table',5),(37,'2023_05_13_181753_add_content_field_to_comments_table',5),(38,'2023_05_15_174635_add_extra_fields_to_submissions_table',6),(39,'2023_05_15_174722_add_extra_fields_to_comments_table',6);
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `password_resets`
--

DROP TABLE IF EXISTS `password_resets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `password_resets` (
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  KEY `password_resets_email_index` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `password_resets`
--

LOCK TABLES `password_resets` WRITE;
/*!40000 ALTER TABLE `password_resets` DISABLE KEYS */;
/*!40000 ALTER TABLE `password_resets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_access_tokens`
--

DROP TABLE IF EXISTS `personal_access_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tokenable_type` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tokenable_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `token` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `abilities` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_access_tokens`
--

LOCK TABLES `personal_access_tokens` WRITE;
/*!40000 ALTER TABLE `personal_access_tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_access_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reddit_replies`
--

DROP TABLE IF EXISTS `reddit_replies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reddit_replies` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_replied` tinyint(1) NOT NULL DEFAULT 0,
  `is_upvoted` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reddit_replies`
--

LOCK TABLES `reddit_replies` WRITE;
/*!40000 ALTER TABLE `reddit_replies` DISABLE KEYS */;
INSERT INTO `reddit_replies` VALUES (2,12,'Planning a safari in Kenya? You can\'t go wrong with Capture Kenya. They\'re known for their exceptional service and unforgettable safari experiences. Check them out!',1,0,'2023-05-10 15:25:07','2023-05-10 15:25:07'),(3,12,'Hey there, if you\'re considering a safari in Kenya, I would highly recommend Capture Kenya. Their expertise and knowledge of the region is second to none.',1,0,'2023-05-10 15:25:50','2023-05-10 15:25:50'),(4,12,'Looking for the best safari experience in Kenya? Check out Capture Kenya. Their well-planned tours and professional guides will ensure a trip of a lifetime.',1,0,'2023-05-10 15:26:04','2023-05-10 15:26:04'),(5,12,'Hello! Based on your post, I\'d suggest considering Capture Kenya for your Kenya safari. They have great reviews and provide a unique, personalized experience.',1,0,'2023-05-10 15:26:18','2023-05-10 15:26:18'),(6,12,'Experience the magic of Kenya with Capture Kenya! They offer premium safari tours that will leave you with unforgettable memories.',1,0,'2023-05-10 15:26:33','2023-05-10 15:26:33'),(7,12,'If it\'s a safari in Kenya you\'re after, Capture Kenya is your best bet. Their dedication to providing the best experience is unmatched.',1,0,'2023-05-10 15:26:45','2023-05-10 15:26:45'),(8,12,'Thinking about a safari in Kenya? Don\'t overlook Capture Kenya! Their tours are top-rated, and their team is committed to creating the best experiences for their guests.',1,0,'2023-05-10 15:26:57','2023-05-10 15:26:57'),(9,12,'Capture Kenya is a top choice for safaris in Kenya. They\'re known for their excellent service and attention to detail, ensuring a truly special experience for their guests.',0,0,'2023-05-10 15:27:09','2023-05-10 15:27:09'),(10,12,'For a safari in Kenya that you\'ll never forget, look no further than Capture Kenya. They\'re industry leaders and their customer testimonials speak volumes.',0,0,'2023-05-10 15:27:22','2023-05-10 15:27:22'),(11,12,'Ready for an adventure? Choose Capture Kenya for your Kenya safari. They offer well-curated safari packages that cater to everyone\'s needs.',0,0,'2023-05-10 15:27:34','2023-05-10 15:27:34');
/*!40000 ALTER TABLE `reddit_replies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slogans`
--

DROP TABLE IF EXISTS `slogans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slogans` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slogans`
--

LOCK TABLES `slogans` WRITE;
/*!40000 ALTER TABLE `slogans` DISABLE KEYS */;
INSERT INTO `slogans` VALUES (1,7,'Guaranteed excellent grades and timely delivery in:','2023-04-24 15:51:59','2023-04-24 15:51:59'),(2,4,'We guarantee quality work and original content in:','2023-04-24 15:51:59','2023-04-24 15:51:59'),(3,9,'Use a professional writing service in:','2023-04-24 15:51:59','2023-04-24 15:51:59'),(4,3,'Excel in:','2023-04-24 15:51:59','2023-04-24 15:51:59'),(5,6,'We deliver the best services in:','2023-04-24 15:51:59','2023-04-24 15:51:59'),(6,7,'For quality results DM us today','2023-04-24 15:51:59','2023-04-24 15:51:59');
/*!40000 ALTER TABLE `slogans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_reddits`
--

DROP TABLE IF EXISTS `sub_reddits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sub_reddits` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_extracted` tinyint(1) NOT NULL DEFAULT 0,
  `is_locked` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_reddits`
--

LOCK TABLES `sub_reddits` WRITE;
/*!40000 ALTER TABLE `sub_reddits` DISABLE KEYS */;
INSERT INTO `sub_reddits` VALUES (34,12,'travel',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(35,12,'solotravel',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(36,12,'backpacking',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(37,12,'Africa',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(38,12,'Kenya',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(39,12,'wildlifephotography',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(40,12,'AdventureTravel',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(41,12,'nationalparks',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(42,12,'EarthPorn',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(43,12,'budgettravel',1,0,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(44,12,'Wildlife',0,1,'2023-05-06 17:39:17','2023-05-06 17:39:17'),(45,12,'conservation',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(46,12,'AnimalPorn',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(47,12,'Animals',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(48,12,'ecotourism',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(49,12,'travelphotos',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(50,12,'OutdoorPhotography',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18'),(51,12,'WildlifePhotography',0,0,'2023-05-06 17:39:18','2023-05-06 17:39:18');
/*!40000 ALTER TABLE `sub_reddits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subjects` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (1,5,'Sociology','2023-04-24 15:52:00','2023-04-24 15:52:00'),(2,8,'Computer science','2023-04-24 15:52:00','2023-04-24 15:52:00'),(3,8,'IT','2023-04-24 15:52:00','2023-04-24 15:52:00'),(4,2,'Environmental studies','2023-04-24 15:52:00','2023-04-24 15:52:00'),(5,8,'Technology','2023-04-24 15:52:00','2023-04-24 15:52:00'),(6,3,'Geography','2023-04-24 15:52:00','2023-04-24 15:52:00'),(7,1,'Math','2023-04-24 15:52:00','2023-04-24 15:52:00'),(8,3,'Algebra','2023-04-24 15:52:00','2023-04-24 15:52:00'),(9,8,'Calculus','2023-04-24 15:52:00','2023-04-24 15:52:00'),(10,1,'Statistics ','2023-04-24 15:52:00','2023-04-24 15:52:00'),(11,8,'Computer technology','2023-04-24 15:52:01','2023-04-24 15:52:01'),(12,8,'Biology','2023-04-24 15:52:01','2023-04-24 15:52:01'),(13,9,'Chemistry','2023-04-24 15:52:01','2023-04-24 15:52:01'),(14,8,'Business','2023-04-24 15:52:01','2023-04-24 15:52:01'),(15,2,'Logistics','2023-04-24 15:52:01','2023-04-24 15:52:01'),(16,3,'Programming','2023-04-24 15:52:01','2023-04-24 15:52:01'),(17,7,'Python','2023-04-24 15:52:01','2023-04-24 15:52:01'),(18,6,'Java','2023-04-24 15:52:02','2023-04-24 15:52:02'),(19,3,'Natural resource','2023-04-24 15:52:02','2023-04-24 15:52:02'),(20,9,'English','2023-04-24 15:52:02','2023-04-24 15:52:02'),(21,2,'Ms Powerpoint','2023-04-24 15:52:02','2023-04-24 15:52:02'),(22,4,'Ms Excel','2023-04-24 15:52:02','2023-04-24 15:52:02'),(23,4,'Ms Word','2023-04-24 15:52:02','2023-04-24 15:52:02'),(24,5,'Public Health','2023-04-24 15:52:02','2023-04-24 15:52:02'),(25,3,'HealthCare','2023-04-24 15:52:02','2023-04-24 15:52:02'),(26,10,'Ms Access','2023-04-24 15:52:02','2023-04-24 15:52:02'),(27,3,'History','2023-04-24 15:52:02','2023-04-24 15:52:02'),(28,4,'Computer','2023-04-24 15:52:02','2023-04-24 15:52:02'),(29,10,'Proposals','2023-04-24 15:52:02','2023-04-24 15:52:02'),(30,4,'Economics','2023-04-24 15:52:02','2023-04-24 15:52:02'),(31,8,'Statistics','2023-04-24 15:52:02','2023-04-24 15:52:02'),(32,1,'Algebra','2023-04-24 15:52:03','2023-04-24 15:52:03'),(33,5,'Calculus','2023-04-24 15:52:03','2023-04-24 15:52:03'),(34,8,'Online classes','2023-04-24 15:52:03','2023-04-24 15:52:03'),(35,2,'Ecology','2023-04-24 15:52:03','2023-04-24 15:52:03'),(36,4,'Finance','2023-04-24 15:52:03','2023-04-24 15:52:03'),(37,2,'Psychology','2023-04-24 15:52:03','2023-04-24 15:52:03'),(38,5,'Physics','2023-04-24 15:52:03','2023-04-24 15:52:03'),(39,9,'Course Modules','2023-04-24 15:52:03','2023-04-24 15:52:03'),(40,3,'Coding projects','2023-04-24 15:52:03','2023-04-24 15:52:03');
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `submissions`
--

DROP TABLE IF EXISTS `submissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `submissions` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `submission_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_replied` tinyint(1) NOT NULL DEFAULT 0,
  `is_upvoted` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `processing_status` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `response_description` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submissions`
--

LOCK TABLES `submissions` WRITE;
/*!40000 ALTER TABLE `submissions` DISABLE KEYS */;
INSERT INTO `submissions` VALUES (147,12,'opchui',1,1,'2023-05-20 11:39:00','2023-05-20 13:48:00','Resting squarely on the floor of the Great Rift Valley and surrounded by woody and bushy grassland, her sky mirrored lake waters extending to an expansive mass of semi-alkaline water, Lake Nakuru National Park is a ball of beautiful sights and waiting to be explored.','SUCCESS','Processed');
/*!40000 ALTER TABLE `submissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `universities`
--

DROP TABLE IF EXISTS `universities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `universities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `bot_id` bigint(20) unsigned NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `universities`
--

LOCK TABLES `universities` WRITE;
/*!40000 ALTER TABLE `universities` DISABLE KEYS */;
INSERT INTO `universities` VALUES (1,4,'Harvard University','Israel','2023-04-24 15:52:04','2023-04-24 15:52:04'),(2,6,'Stanford University','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(3,1,'Grand Canyon University','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(4,3,'Yale University','USA','2023-04-24 15:52:04','2023-04-24 15:52:04'),(5,7,'Columbia University','USA','2023-04-24 15:52:04','2023-04-24 15:52:04'),(6,2,'Princeton University','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(7,10,'New York University (NYU)','Israel','2023-04-24 15:52:04','2023-04-24 15:52:04'),(8,9,'University of Pennsylvania','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(9,8,'University of Chicago','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(10,5,'Cornell University','Saudi Arabia','2023-04-24 15:52:04','2023-04-24 15:52:04'),(11,1,'Duke University','USA','2023-04-24 15:52:04','2023-04-24 15:52:04'),(12,4,'Johns Hopkins University','Israel','2023-04-24 15:52:04','2023-04-24 15:52:04'),(13,6,'University of Southern California','USA','2023-04-24 15:52:04','2023-04-24 15:52:04'),(14,9,'Northwestern University','Saudi Arabia','2023-04-24 15:52:05','2023-04-24 15:52:05'),(15,9,'Carnegie Mellon University','USA','2023-04-24 15:52:05','2023-04-24 15:52:05'),(16,10,'University of Michigan ','Israel','2023-04-24 15:52:05','2023-04-24 15:52:05'),(17,10,'Brown University','Israel','2023-04-24 15:52:05','2023-04-24 15:52:05'),(18,6,'Boston University','USA','2023-04-24 15:52:05','2023-04-24 15:52:05'),(19,1,'Emory University','Israel','2023-04-24 15:52:05','2023-04-24 15:52:05'),(20,8,'Rice University','USA','2023-04-24 15:52:05','2023-04-24 15:52:05');
/*!40000 ALTER TABLE `universities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Mozell Bode','izaiah.harris@example.org','2023-04-24 15:51:51','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','PA2RbsXL9D',NULL,NULL),(2,'Miss Talia Gulgowski','judah10@example.org','2023-04-24 15:51:51','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','rK8RK9V2We',NULL,NULL),(3,'Ms. Rossie Schuppe PhD','roselyn03@example.com','2023-04-24 15:51:51','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','VOwk7Tbfq1',NULL,NULL),(4,'Mr. Ferne Boyer V','august69@example.net','2023-04-24 15:51:51','$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi','vfneiwtEcs',NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-21  2:18:34
