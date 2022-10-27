drop database bookings;
CREATE database IF NOT EXISTS `Bookings` DEFAULT CHARACTER SET utf8 ;
USE `Bookings` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bookings`.`Usuario` (
  `idUsuario` varchar(20) NOT NULL,
  `nombreUsuario` VARCHAR(45) NULL,
  `apellidoUsuario` VARCHAR(45) NULL,
  `direccionUsuario` VARCHAR(80) NULL,
  `emailUsuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE INDEX `emailUsuario_UNIQUE` (`emailUsuario` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Hotel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bookings`.`Hotel` (
  `idHotel` INT NOT NULL AUTO_INCREMENT,
  `nombreHotel` VARCHAR(45) NOT NULL,
  `paisHotel` VARCHAR(45) NOT NULL,
  `latitudHotel` float NOT NULL,
  `longitudHotel` float NOT NULL,
  `descripciónHotel` VARCHAR(150) NULL,
  `activoHotel` TINYINT NOT NULL,
  PRIMARY KEY (`idHotel`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Habitacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bookings`.`Habitacion` (
  `idHabitacion` INT NOT NULL AUTO_INCREMENT,
  `Hotel_idHotel` INT NOT NULL,
  PRIMARY KEY (`idHabitacion`),
  INDEX `fk_Habitacion_Hotel1_idx` (`Hotel_idHotel` ASC) VISIBLE,
  CONSTRAINT `fk_Habitacion_Hotel1`
    FOREIGN KEY (`Hotel_idHotel`)
    REFERENCES `Bookings`.`Hotel` (`idHotel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Bookings`.`Reserva` (
  `idReserva` INT NOT NULL AUTO_INCREMENT,
  `checkin` DATE NOT NULL,
  `checkout` DATE NOT NULL,
  `fechaReserva` DATE NOT NULL,
  `estadoReserva` VARCHAR(45) NULL,
  `Usuario_idUsuario` varchar(20) NOT NULL,
  `Habitacion_idHabitacion` INT NOT NULL,
  PRIMARY KEY (`idReserva`),
  INDEX `fk_Reserva_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  INDEX `fk_Reserva_Habitacion1_idx` (`Habitacion_idHabitacion` ASC) VISIBLE,
  CONSTRAINT `fk_Reserva_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `Bookings`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reserva_Habitacion1`
    FOREIGN KEY (`Habitacion_idHabitacion`)
    REFERENCES `Bookings`.`Habitacion` (`idHabitacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;