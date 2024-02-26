-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema rentingdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema rentingdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rentingdb` DEFAULT CHARACTER SET utf8 ;
USE `rentingdb` ;

-- -----------------------------------------------------
-- Table `rentingdb`.`Renter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rentingdb`.`Renter` (
  `renter_id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(2) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`renter_id`),
  UNIQUE INDEX `renter_id_UNIQUE` (`renter_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rentingdb`.`Sellers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rentingdb`.`Sellers` (
  `sellers_id` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NOT NULL,
  `lname` VARCHAR(45) NOT NULL,
  `street_address` VARCHAR(45) NOT NULL,
  `city` VARCHAR(45) NOT NULL,
  `state` VARCHAR(2) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`sellers_id`),
  UNIQUE INDEX `Sellers_id_UNIQUE` (`sellers_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rentingdb`.`Requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rentingdb`.`Requests` (
  `requests_id` INT NOT NULL AUTO_INCREMENT,
  `request_name` VARCHAR(50) NOT NULL,
  `renter_id` INT NOT NULL,
  PRIMARY KEY (`requests_id`),
  UNIQUE INDEX `name_UNIQUE` (`request_name` ASC) VISIBLE,
  UNIQUE INDEX `Requests_id_UNIQUE` (`requests_id` ASC) VISIBLE,
  INDEX `fk_Requests_renter_idx` (`renter_id` ASC) VISIBLE,
  CONSTRAINT `fk_Requests_renter`
    FOREIGN KEY (`renter_id`)
    REFERENCES `rentingdb`.`Renter` (`renter_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rentingdb`.`Listings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `rentingdb`.`Listings` (
  `listings_id` INT NOT NULL AUTO_INCREMENT,
  `item` VARCHAR(100) NOT NULL,
  `price` DECIMAL NOT NULL,
  `sellers_id` INT NOT NULL,
  PRIMARY KEY (`listings_id`),
  UNIQUE INDEX `Listings_id_UNIQUE` (`listings_id` ASC) VISIBLE,
  INDEX `fk_Listings_Sellers1_idx` (`sellers_id` ASC) VISIBLE,
  CONSTRAINT `fk_Listings_Sellers1`
    FOREIGN KEY (`sellers_id`)
    REFERENCES `rentingdb`.`Sellers` (`sellers_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
