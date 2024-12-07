-- Create the Database
CREATE DATABASE OutlandAdventuresDB;

-- Create a new MySQL user
CREATE USER IF NOT EXISTS 'mytestuser'@'localhost' IDENTIFIED BY 'mytestuser';

-- Grant privileges to the user for the OutlandAdventuresDB database
GRANT ALL PRIVILEGES ON OutlandAdventuresDB.* TO 'mytestuser'@'localhost';

-- Apply the privilege changes
FLUSH PRIVILEGES;

-- Use the Database
USE OutlandAdventuresDB;

-- Create Trips Table
CREATE TABLE IF NOT EXISTS Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,
    Destination VARCHAR(100),
    StartDate DATE,
    EndDate DATE,
    PreparationRequirements TEXT,
    InventoryID INT
);

-- Create Guides Table
CREATE TABLE IF NOT EXISTS Guides (
    GuideID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Responsibilities TEXT
);

-- Create TripGuides Table (Link Table for M:N Relationship)
CREATE TABLE IF NOT EXISTS TripGuides (
    TripID INT,
    GuideID INT,
    PRIMARY KEY (TripID, GuideID),
    FOREIGN KEY (TripID) REFERENCES Trips(TripID),
    FOREIGN KEY (GuideID) REFERENCES Guides(GuideID)
);

-- Create Customers Table
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    PaymentInfo TEXT
);

-- Create Bookings Table
CREATE TABLE IF NOT EXISTS Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    TripID INT,
    CustomerID INT,
    BookingDate DATE,
    PaymentStatus VARCHAR(50),
    FOREIGN KEY (TripID) REFERENCES Trips(TripID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create Equipment Table
CREATE TABLE IF NOT EXISTS Equipment (
    EquipmentID INT AUTO_INCREMENT PRIMARY KEY,
    Category VARCHAR(100),
    Description TEXT,
    PurchaseDate DATE,
    ItemCondition VARCHAR(50),
    Availability VARCHAR(50)
);

-- Create Inventory Table
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
    EquipmentID INT,
    LastInspectionDate DATE,
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)
);

-- Create Marketing Table
CREATE TABLE IF NOT EXISTS Marketing (
    CampaignID INT AUTO_INCREMENT PRIMARY KEY,
    Destination VARCHAR(100),
    BookingTrends TEXT,
    FinancialEfficiency DECIMAL(10, 2),
    MarketTrends TEXT
);

-- Create Administration Table
CREATE TABLE IF NOT EXISTS Administration (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    StaffName VARCHAR(100),
    Role VARCHAR(100),
    Responsibilities TEXT
);

-- Create E-commerce Site Table
CREATE TABLE IF NOT EXISTS EcommerceSite (
    SiteID INT AUTO_INCREMENT PRIMARY KEY,
    TripDetails TEXT,
    EquipmentListings TEXT,
    SalesTracking TEXT
);

-- Populate Tables with Funny Data
INSERT INTO Trips (Destination, StartDate, EndDate, PreparationRequirements, InventoryID)
VALUES ('Africa: Safari & Shenanigans', '2024-01-10', '2024-01-20', 'Pack Extra Patience for Bureaucracy', 1),
       ('Asia: Rice Fields & Riddles', '2024-02-15', '2024-02-25', 'Survive Without Wi-Fi Challenge', 2),
       ('Southern Europe: Siestas & Sangria', '2024-03-01', '2024-03-10', 'Mosquito Survival Training Required', 3);

INSERT INTO Guides (Name, Responsibilities)
VALUES ('John "Jungle John" Viney', 'Trip Planning and Coordination'),
       ('Emily "Eagle Eyes" Smithers', 'Navigation and Wildlife Spotting'),
       ('Barry "Barely Prepared" Baxter', 'Supply Management and Jokes'),
       ('Sheila "Shortcut Queen" Dawson', 'Trail Shortcuts and Fun Stories'),
       ('Duke "Don\'t Ask for Directions" Marland', 'Logistics and Customer Humor');

INSERT INTO TripGuides (TripID, GuideID)
VALUES (1, 1), (1, 2), (2, 3), (3, 4), (3, 5);

INSERT INTO Customers (Name, Email, Phone, PaymentInfo)
VALUES ('Karen "Can I Speak to Your Manager?" Jones', 'karen.manager@example.com', '123-456-7890', 'Credit Card'),
       ('Chad "Selfie Stick Extraordinaire" Bradley', 'chad.selfie@example.com', '987-654-3210', 'PayPal'),
       ('Patty "Pack-It-All" McStufferson', 'patty.pack@example.com', '555-666-7777', 'Debit Card'),
       ('Dale "Discount Dave" Bargain', 'dale.deals@example.com', '444-888-9999', 'Bitcoin'),
       ('Zoe "Zen and Out of Service" Chillman', 'zoe.chill@example.com', '333-222-1111', 'Cash'),
       ('Bart "Bargain Bob" Rollins', 'bart.bargain@example.com', '111-222-3333', 'Gift Card');

INSERT INTO Bookings (TripID, CustomerID, BookingDate, PaymentStatus)
VALUES (1, 1, '2023-12-01', 'Paid'),
       (1, 2, '2023-12-03', 'Pending'),
       (2, 3, '2023-12-05', 'Paid'),
       (2, 4, '2023-12-07', 'Pending'),
       (3, 5, '2023-12-10', 'Paid'),
       (3, 6, '2023-12-12', 'Pending');

INSERT INTO Equipment (Category, Description, PurchaseDate, ItemCondition, Availability)
VALUES ('Mega Cozy Sleeping Bag 3000', 'Super thermal sleeping bag for Arctic expeditions', '2020-01-01', 'Good', 'Available'),
       ('Invisible Tent Deluxe', 'A tent so good, you can barely see it!', '2019-06-01', 'Excellent', 'Unavailable'),
       ('Fire Starter Pro™', 'Guaranteed to work... eventually', '2018-03-15', 'Fair', 'Available'),
       ('Mosquito Net of Destiny', 'Keeps the bugs AND bad dreams away', '2021-05-20', 'Good', 'Available'),
       ('Waterproof Backpack of Holding', 'Infinite storage for hikers', '2022-08-10', 'Excellent', 'Available');

INSERT INTO Inventory (EquipmentID, LastInspectionDate)
VALUES (1, '2023-06-01'), (2, '2023-07-01'), (3, '2023-08-01'), (4, '2023-09-01'), (5, '2023-10-01');

INSERT INTO Marketing (Destination, BookingTrends, FinancialEfficiency, MarketTrends)
VALUES ('Africa: Safari & Shenanigans', 'Increasing', 80.5, 'High Demand'),
       ('Asia: Rice Fields & Riddles', 'Stable', 70.2, 'Moderate Demand'),
       ('Southern Europe: Siestas & Sangria', 'Decreasing', 50.8, 'Low Demand');

INSERT INTO Administration (StaffName, Role, Responsibilities)
VALUES ('Jim Ford', 'Inventory Manager', 'Monthly Inventory Updates'),
       ('Blythe Timmerson', 'Financial Officer', 'Budgeting and Financial Records');

INSERT INTO EcommerceSite (TripDetails, EquipmentListings, SalesTracking)
VALUES ('Detailed Africa Trip Info', 'Mega Cozy Sleeping Bag 3000, Invisible Tent Deluxe', 'Track Sales and Rentals');
