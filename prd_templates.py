prdFormat = """
1. Introduction

1.1 Test Objectives

      The system integration test of the XYZ system should validate from both the requirements
      perspective and business perspective that:

      •        All payroll business processes are supported.
      •        All timekeeping functions work correctly.
      •        Direct deposit functions work correctly.
      •        Payroll functions work correctly.
      •        The system is easy to use by the end-users.
      •        Payroll policies and procedures are supported by the system.
      •        The system can be customized by remote offices to handle localized payroll processing
               needs.
      •        The system complies with all government payroll tax reporting format requirements.
      •        Financial controls are adequate to prevent fraudulent transactions.
      •        Security controls are in place to prevent unauthorized system access.
      •        All financial calculations are correct.
      •        All points of integration within the system work as defined in requirements.
      •        All points of integration with other systems work as defined in requirements.
      •        Recovery procedures are correct and can be performed by users.

      The objective of system integration testing is to validate the system operation as a whole and with
      other systems. At the conclusion of testing, the project team and the test team will have a high
      level of confidence that the system will work according to user requirements and will meet
      business needs.

1.2 Scope of Testing

      The system integration test of the XYZ system will include payroll, accounting, and timekeeping
      applications. In addition, the interfaces to remote offices and the Internal Revenue Service will be
      tested.

      The system integration test of the XYZ system will not include system administration functions.




Page 4 of 15           Copyright, Rice Consulting Services, Inc.                  11/14/2019 6:58:00 AM
                 Sample System Integration Test Plan - XYZ Remote Office Payroll System


1.3 System Overview

      The XYZ system is a company-wide application that accepts
      personnel and payroll information from each of the                                             Remote
                                                                                                     Offices
      company’s 50 remote offices across the U.S., processes
      payroll and produces payroll reports. The XYZ system will be
      networked to each of the remote offices and will link to the
      Internal Revenue Service by modem to transmit payroll tax
      deposits and tax reports.                                                       Timekeeping
                                                                                      Applications




                                                                              Payroll            Accounting
                                                                            Applications         Applications




                                                                                IRS                  Reports
1.4 Definitions/Acronyms


1.4.1 Definitions

  Build                       A functionally independent piece of software that supports a well-defined
                              logical subset of a system. A build can be tested independently and then
                              integrated with other builds. Builds can be migrated from one level of testing
                              to another and possibly installed independently of the rest of the system.
  Critical Processing         A program, module or unit that is critical to the correct functioning of the
  Unit                        system. A critical processing unit carries with it a high impact of failure.
  Model Office                A validation of the implementation, operation and training of the system in a
                              simulated office environment.
  Prototype                   A working model of the software to be built. Demonstrates look and feel of
                              the software, but does not support all features and functions.
  Regression Testing          Testing to ensure that unchanged parts of the software work the same as
                              before a change was made.
  Requirement                 Something that the system should do or be. May be based on user,
                              business, or technical needs.
  Static Test                 A verification performed without execution on a computer. For example,
                              reviewing a document for accuracy.
  System Integration          A level of testing that validates both internal and external system interfaces,
  Testing                     ensuring that the system works as a cohesive whole. The purpose of
                              systems integration testing is to perform test cases that validate the system
                              was built according to requirements.
  Test Tool                   Any vehicle that assists in testing.
  Unit Testing                A level of testing in which the smallest units of a system (i.e., modules) are
                              separately tested.
  Unit-to-Unit Testing        A level of testing that validates the integration between groups of related
                              modules or units.




Page 5 of 15             Copyright, Rice Consulting Services, Inc.                  11/14/2019 6:58:00 AM
               Sample System Integration Test Plan - XYZ Remote Office Payroll System


1.4.2 Acronyms

  FICA                       Federal Income Tax
  FUTA                       Federal Unemployment Tax
  IRS                        Internal Revenue Service
  SSN                        Social Security Number


1.5 References

      •        Requirements Specification Document for the XYZ System
      •        Test Standards
      •        Test Procedures
      •        Test Plan Notebook
      •        Payroll Policy and Procedures Notebook


2. Approach

2.1 Assumptions/Constraints

2.1.1 Assumptions

      •        The first build of the XYZ system will be ready for system integration testing on
               July 1, XXXX.
      •        Each build of the XYZ system will have passed unit and unit-to-unit testing before it is
               transferred to the system integration testing environment.

2.1.2 Constraints

      •        Six weeks might not be enough time to test the entire system and then retest the system
               to find new defects due to fixes.

2.2 Coverage

      Test coverage will be measured by:

      •        A completed matrix of testable requirements and test cases.

      •        A completed matrix of business processes and business test cases.

      In the event that coverage levels are not met, the QA manager will determine if the actual levels
      are adequate in light of the system risks.

2.2.1 Software Components

      All software modules in the payroll, timekeeping, and accounting sub-systems will be tested.

2.2.2 Requirements

      All user requirements as specified in the Requirements Specification Document will be tested.



Page 6 of 15           Copyright, Rice Consulting Services, Inc.                  11/14/2019 6:58:00 AM
               Sample System Integration Test Plan - XYZ Remote Office Payroll System




2.2.3 Business Processes

      All critical business processes will be validated completely. Critical business processes are:

      •        Employee Time Entry
      •        Payroll Tax Calculation
      •        Create Paychecks
      •        Direct Deposit
      •        Submit Payroll Withholding Reports to the IRS.

2.3 Test Tools

      •        Capture/Playback
      •        Test Manager
      •        Defect Tracker

2.4 Test Type (Regression, Conversion, etc.)

      The following types of testing will be performed during system integration testing:

      •        Functional testing, by performing test cases based on testable requirements
      •        Functional testing, by performing test cases based on business functions
      •        Compliance testing, by evaluating system performance against company policies and
               procedures
      •        Security testing, by testing each end-user’s security access levels
      •        Controls testing, by testing all financial controls
      •        Regression testing, to ensure that a change to the system does not introduce new
               defects.
      •        Recovery testing, to ensure the system can be restarted by the end user in the event of a
               system failure.

2.5 Test Data

      To perform system integration testing, test data will be supplied from two sources:

      •        Data created specifically for the system integration test and
      •        Data obtained from past payroll periods.

      The order of test execution allows for test data to be created before it is needed in payroll
      processing and payroll reporting.

      The following test data sources will be located on the central server in the test environment:

      •        Employee data table (EMPLOYEE) - converted from existing sequential files and
               supplemented with specific test data that will execute test cases.
      •        Employee time data (EMPTIME) - entered during the test and converted from existing
               sequential files
      •        Tax table for current year and next year (TAXTABLE) - obtained in electronic format from
               the IRS.




Page 7 of 15            Copyright, Rice Consulting Services, Inc.                  11/14/2019 6:58:00 AM
                Sample System Integration Test Plan - XYZ Remote Office Payroll System


3. Plan

3.1 Test Team

      The following people will be on the system integration test team:

          Name            Title                 Level of involvement       Responsibilities
          Joe Johnson     Team Leader -         40 hrs/wk                  Lead all testing activities,
                          Independent Test                                 including test planning, test
                          Team                                             execution, and status reporting.
          Mary            Assistant Team        40 hrs/wk                  Fill in during any absence of
          Anderson        Leader -                                         team leader. Design and
                          Independent Test                                 execute test cases, create test
                          Team                                             data, write test summary report
          Pete Wilson     End user - Payroll    25 hrs/wk                  Design and execute test cases
                          Dept.                                            for payroll processing.
          Tom Jones       End user - Internal   40 hrs/wk                  Design and execute test cases
                          Audit Dept.                                      to validate financial controls
          Jane            End user -            30 hrs/wk                  Design and execute test cases,
          Peterson        Personnel Dept.                                  build employee test tables
          Doug            Independent           40 hrs/wk                  Design and execute test cases
          Thompson        Tester                                           for time reporting.
          Dot Wong        Independent           40 hrs/wk                  Design and execute test cases
                          Tester                                           for payroll direct deposit.
          Renee           Independent           40 hrs/wk                  Design test cases for payroll
          Roberts         Tester                                           reporting to IRS and financial
                                                                           sub-system.
          Gary Moore      Developer             40 hrs/wk                  Technical assistance as
                                                                           needed during the test


3.2 Team Reviews

      The following reviews will be conducted by the entire test team and a representative from the QA
      department. Refer to the work schedule for the planned review dates.

      •          Test plan review
      •          Test case review
      •          Test progress review
      •          Post-test review

3.3 Major Tasks and Deliverables


          Task                              Start           Stop          Deliverable(s)
          System integration test case      5/1/XXXX        6/1/XXXX      System integration test cases
          design
          Build system integration test     5/15/XXXX       6/15/XXXX     Test environment ready for test
          environment                                                     data population
          Build system integration test     6/2/XXXX        6/15/XXXX     Employee data table, Employee
          data                                                            time data, Tax table for current
                                                                          year and next year.



Page 8 of 15             Copyright, Rice Consulting Services, Inc.              11/14/2019 6:58:00 AM
                Sample System Integration Test Plan - XYZ Remote Office Payroll System


          Task                              Start         Stop          Deliverable(s)
          Train test team                   6/15/XXXX     6/17/XXXX     Trained testers
          Build 1 delivered for system                    6/29/XXXX     Build 1 ready for system
          integration testing                                           integration testing.
          Build 1 test execution            7/1/XXXX      7/15/XXXX     Build 1 tested
          Build 1 test summary report due                 7/17/XXXX     Build 1 test summary report
          Build 2 test execution            7/18/XXXX     7/26/XXXX     Build 2 tested
          Build 2 test summary report due                 7/28/XXXX     Build 2 test summary report
          Build 3 test execution            8/1/XXXX      8/15/XXXX     Build 3 tested
          Build 3 test summary report due                 8/17/XXXX     Build 3 test summary report
          System migration to model         8/20/XXXX     8/22/XXXX     Installed system
          office environment


3.4 Environmental Needs

3.4.1 Test Environment

      Hardware
      All test cases will be executed on the Development Server in the QA database environment.

      •        One (1) networked HP Laser Jet printer.

      (2) Asus
      Intel Core i5-4460S
      8GB DDR3 RAM:
      24X Super-Multi DVD/RW drive

      (2) Dell Inspiron 3000
      Intel® Pentium® G3240 dual-core 3.1 GHz 3MB cache processor
      4GB RAM DDR3 1600 SDRAM memory
      1TB 7200 RPM serial ATA/600 hard drive, controller type: serial ATA

      (2) iMAC
      1.4GHz
      dual-core Intel Core i5 processor (Turbo Boost up
      to 2.7GHz) with 3MB shared L3 cache
      8GB of 1600MHz LPDDR3 onboard memory
      500GB (5400-rpm) hard drive

      Network

      •        LAN
                 - Synoptic 810 10Base-T Ethernet Concentrator
                 - Category 5 cables to meet 10Base-T specifications

      Software

      •        XYZ application software

      •      Server
      - GreenTree Accounting version 3.0
      - MS Windows 7 Pro operating system
      - MS Windows 8 Pro operating system



Page 9 of 15            Copyright, Rice Consulting Services, Inc.             11/14/2019 6:58:00 AM
                 Sample System Integration Test Plan - XYZ Remote Office Payroll System


3.4.2 Test Lab

        The following items will be needed full-time by the system integration test team:

        •       1 whiteboard (large) with markers and erasers
        •       Clerical/organizational material - file cabinet, storage boxes, folders, notebooks

        NOTE: The aforementioned items are in addition to the hardware and software items detailed in
        Section 3.4.1.


3.5 Training

        Test team members who have not been trained in the testing process will be trained in testing
        techniques by the QA staff. The training will be three days in length and will be conducted at the
        corporate training facility the dates of 6/15/XXXX - 6/17/XXXX.


4. Features to be Tested

4.1 Build 1

4.1.1    Table Maintenance

         •        Update project code table entries
         •        Update department code entries
         •        Add/Update office codes
         •        Security (authorization levels for table maintenance)
         •        Security (authorization and access for system users)

4.1.2    Create Timesheets

         •        First timesheet
         •        Last timesheet
         •        Partial period timesheet
         •        Security
         •        Controls

4.1.3    Employee Time Entry

         •        Overtime entry
         •        Incomplete entry of time worked
         •        Normal entry of time worked
         •        Security
         •        Controls

4.1.4    System Ease of Use

         •        Navigation
         •        Help functions
         •        Order of processing



Page 10 of 15             Copyright, Rice Consulting Services, Inc.                  11/14/2019 6:58:00 AM
                Sample System Integration Test Plan - XYZ Remote Office Payroll System


4.1.5 System Performance

        •       Response time for employee time entry
        •       Transaction throughput time for timesheet creation

4.2 Build 2

4.2.1   Payroll Tax Calculation

        •       FICA
        •       Medicare
        •       Unemployment (FUTA)
        •       State Income Tax
        •       Financial controls

4.2.2   Create Paychecks

        •       Withholding reconciliation
        •       YTD totals
        •       Calculations
        •       Financial controls
        •       Security

4.2.3 Accounting Reports and General Ledger Interface (GreenTree Accounting software)
       •      Gross pay and withholdings
       •      Payroll reconciliation
       •      Journal listing
       •      GL account listing
       •      GL report
       •      GL transaction reconciliation
       •      Security
       •      Financial controls

4.2.4   System Ease of Use

        •       Navigation
        •       Help functions
        •       Order of processing

4.2.5 System Performance

        •       Response time for GreenTree accounting functions
        •       Transaction throughput time for paycheck creation

4.3 Build 3

4.3.1   Direct Deposit

        •       Update employee direct deposit information
        •       Transmit transactions
        •       Reconcile transmission report



Page 11 of 15            Copyright, Rice Consulting Services, Inc.           11/14/2019 6:58:00 AM
                Sample System Integration Test Plan - XYZ Remote Office Payroll System


         •       Security
         •       Financial controls

4.3.2    Submit Payroll Withholding Reports to IRS

         •       Transfer protocol correct
         •       Calculations correct
         •       Transmit payroll reports to the IRS
         •       Transmit weekly payroll tax deposit
         •       Security
         •       Financial controls

4.3.3    System Ease of Use

         •       Navigation
         •       Help functions
         •       Order of processing

4.3.4 System Performance

         •       Transaction throughput time for direct deposit and payroll reporting

4.3.5 Data Recovery

         •       Recovery from remote transmission errors
         •       Recovery from interruptions in batch processing
         •       Recovery from interruptions in online processing
         •       Recovery from General Protection Faults (GPFs)


5. Features Not to be Tested

5.1      System Administration Functions

        •        User Password Administration
        •        File Security Procedures


"""
