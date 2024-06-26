-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema LifeTrack
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LifeTrack
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LifeTrack` DEFAULT CHARACTER SET utf8 ;
USE `LifeTrack` ;

-- -----------------------------------------------------
-- Table `LifeTrack`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LifeTrack`.`todos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`todos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `date` DATE NULL,
  `location` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_todos_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_todos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `LifeTrack`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LifeTrack`.`goals`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`goals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_goals_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_goals_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `LifeTrack`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LifeTrack`.`goals_has_todos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`goals_has_todos` (
  `id` INT NOT NULL,
  `goal_id` INT NOT NULL,
  `todo_id` INT NOT NULL,
  INDEX `fk_goals_has_todos_todos1_idx` (`todo_id` ASC) VISIBLE,
  INDEX `fk_goals_has_todos_goals1_idx` (`goal_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_goals_has_todos_goals1`
    FOREIGN KEY (`goal_id`)
    REFERENCES `LifeTrack`.`goals` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_goals_has_todos_todos1`
    FOREIGN KEY (`todo_id`)
    REFERENCES `LifeTrack`.`todos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LifeTrack`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LifeTrack`.`activities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LifeTrack`.`activities` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `start_time` DATETIME NULL,
  `end_time` DATETIME NULL,
  `location` VARCHAR(45) NULL,
  `notes` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_activities_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_activities_categories1_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_activities_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `LifeTrack`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_activities_categories1`
    FOREIGN KEY (`category_id`)
    REFERENCES `LifeTrack`.`categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
