import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import java.util.Vector;
public class Main extends JFrame {
    private Connection connection;
    private JTable flightTable;
    private DefaultTableModel flightTableModel;
    private JButton bookButton, postButton, searchButton, registerButton;
    private JTextField destinationField, departureField, dateField, usernameField, passwordField,
            nameField, dobField, addressField;
    private JTextArea chatTextArea;
    private JScrollPane chatScrollPane;
    private JPanel mainPanel, loginPanel;
    private boolean loggedIn = false;
    private int loggedInUserId;
    private String loggedInUsername;
    public Main() {
        setTitle("Airline Booking App");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
// Login Panel
        loginPanel = new JPanel(new GridLayout(7, 2));
        loginPanel.setBackground(new Color(173, 216, 230)); // Light Blue background
        loginPanel.add(new JLabel("Username:"));
        usernameField = new JTextField();
        loginPanel.add(usernameField);
        loginPanel.add(new JLabel("Password:"));
        passwordField = new JPasswordField();
        loginPanel.add(passwordField);
        loginPanel.add(new JLabel("Name:"));
        nameField = new JTextField();
        loginPanel.add(nameField);
        loginPanel.add(new JLabel("Date of Birth (YYYY-MM-DD):"));
        dobField = new JTextField();
        loginPanel.add(dobField);
        loginPanel.add(new JLabel("Address:"));
        addressField = new JTextField();
        loginPanel.add(addressField);
        JButton loginButton = new JButton("Login");
        loginPanel.add(loginButton);
        registerButton = new JButton("Register");
        loginPanel.add(registerButton);
        add(loginPanel);
        setVisible(true);
// Connect to the database
        try {
            "ADISHMA");
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/cloud_airline", "root",
        } catch (SQLException e) {
            e.printStackTrace();
        }
// Action Listeners for login panel buttons
        loginButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = usernameField.getText();
                String password = passwordField.getText();
                if (validateLogin(username, password)) {
                    loggedIn = true;
                    loggedInUserId = getUserId(username);
                    loggedInUsername = username;
                    JOptionPane.showMessageDialog(Main.this, "Login successful!");
                    remove(loginPanel);
                    initializeMainPanel();
                } else {
                    JOptionPane.showMessageDialog(Main.this, "Invalid username or password. Please try
                            again.");
                }
            }
        });
        registerButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String username = usernameField.getText();
                String password = passwordField.getText();
                String name = nameField.getText();
                String dob = dobField.getText();
                String address = addressField.getText();
                if (!username.isEmpty() && !password.isEmpty() && !name.isEmpty() && !dob.isEmpty() &&
                        !address.isEmpty()) {
                    if (registerUser(username, password, name, dob, address)) {
                        JOptionPane.showMessageDialog(Main.this, "Registration successful! Please login.");
                    } else {
                        JOptionPane.showMessageDialog(Main.this, "Registration failed! Please try again.");
                    }
                } else {
                    JOptionPane.showMessageDialog(Main.this, "Please enter all fields.");
                }
            }
        });
    }
    private boolean validateLogin(String username, String password) {
        try {
            String query = "SELECT * FROM customer WHERE username = ? AND password = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.next(); // Return true if a row is found
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
    private int getUserId(String username) {
        try {
            String query = "SELECT user_id FROM customer WHERE username = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getInt("user_id");
            } else {
                return -1;
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return -1;
        }
    }
    private boolean registerUser(String username, String password, String name, String dob, String
            address) {
        try {
            String query = "INSERT INTO customer (username, password, name, Date_of_Birth, address)
            VALUES (?, ?, ?, ?, ?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, username);
            statement.setString(2, password);
            statement.setString(3, name);
            statement.setString(4, dob);
            statement.setString(5, address);
            int rowsInserted = statement.executeUpdate();
            return rowsInserted > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }
    private void initializeMainPanel() {
// Main Panel
        mainPanel = new JPanel(new BorderLayout());
        mainPanel.setBackground(Color.WHITE); // White background
// Flight Table
        flightTableModel = new DefaultTableModel();
        flightTableModel.addColumn("Flight ID");
        flightTableModel.addColumn("Airlines");
        flightTableModel.addColumn("Departure");
        flightTableModel.addColumn("Destination");
        flightTableModel.addColumn("Departure Time");
        flightTableModel.addColumn("Arrival Time");
        flightTableModel.addColumn("Price");
        flightTableModel.addColumn("Capacity");
        flightTableModel.addColumn("Flight Type"); // New column for flight type
        flightTable = new JTable(flightTableModel);
        JScrollPane scrollPane = new JScrollPane(flightTable);
// Search Panel
        JPanel searchPanel = new JPanel(new FlowLayout());
        searchPanel.setBackground(new Color(240, 240, 240)); // Light Gray background
        destinationField = new JTextField(10);
        departureField = new JTextField(10);
        dateField = new JTextField(10);
        searchButton = new JButton("Search Flights");
        searchPanel.add(new JLabel("Destination:"));
        searchPanel.add(destinationField);
        searchPanel.add(new JLabel("Departure:"));
        searchPanel.add(departureField);
        searchPanel.add(new JLabel("Date (YYYY-MM-DD):"));
        searchPanel.add(dateField);
        searchPanel.add(searchButton);
// Chat Panel
        JPanel chatPanel = new JPanel(new BorderLayout());
        chatPanel.setBackground(new Color(255, 250, 205)); // LemonChiffon background
        chatTextArea = new JTextArea(10, 50);
        chatScrollPane = new JScrollPane(chatTextArea);
        chatPanel.add(new JLabel("Chat Box"), BorderLayout.NORTH);
        chatPanel.add(chatScrollPane, BorderLayout.CENTER);
// Buttons Panel
        JPanel buttonPanel = new JPanel(new FlowLayout());
        buttonPanel.setBackground(new Color(240, 248, 255)); // AliceBlue background
        bookButton = new JButton("Book Flight");
        postButton = new JButton("Post Message");
        buttonPanel.add(bookButton);
        buttonPanel.add(postButton);
// Add components to main panel
        mainPanel.add(searchPanel, BorderLayout.NORTH);
        mainPanel.add(scrollPane, BorderLayout.CENTER);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);
        mainPanel.add(chatPanel, BorderLayout.SOUTH);
        add(mainPanel);
        setVisible(true);
// Action Listeners
        searchButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String destination = destinationField.getText();
                String departure = departureField.getText();
                String date = dateField.getText();
                searchFlights(destination, departure, date);
            }
        });
        bookButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
// Handle flight booking
                int selectedRow = flightTable.getSelectedRow();
                if (selectedRow != -1) {
                    int flightId = (int) flightTableModel.getValueAt(selectedRow, 0);
                    double price = (double) flightTableModel.getValueAt(selectedRow, 6);
                    String departure = (String) flightTableModel.getValueAt(selectedRow, 2);
                    String destination = (String) flightTableModel.getValueAt(selectedRow, 3);
                    double amountPaid = price; // You can calculate based on additional features
                    generateBill(flightId, departure, destination, amountPaid);
                } else {
                    JOptionPane.showMessageDialog(Main.this, "Please select a flight to book.");
                }
            }
        });
        postButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
// Handle posting message to chat
                String message = JOptionPane.showInputDialog(Main.this, "Enter your message:");
                if (message != null && !message.isEmpty()) {
                    postMessage(message);
                }
            }
        });
// Add a MouseListener to the flightTable
        flightTable.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 1) { // Check if it's a single click
                    JTable target = (JTable) e.getSource();
                    int row = target.getSelectedRow();
                    int column = target.getSelectedColumn();
                    if (row != -1 && column != -1) {
// Perform actions for generating bill and selling ticket
                        int flightId = (int) flightTableModel.getValueAt(row, 0);
                        double price = (double) flightTableModel.getValueAt(row, 6);
                        String departure = (String) flightTableModel.getValueAt(row, 2);
                        String destination = (String) flightTableModel.getValueAt(row, 3);
                        double amountPaid = price; // You can calculate based on additional features
                        generateBill(flightId, departure, destination, amountPaid);
                    }
                }
            }
        });
    }
    private void loadFlights(ResultSet resultSet) throws SQLException {
        flightTableModel.setRowCount(0); // Clear current table data
        while (resultSet.next()) {
            Vector<Object> row = new Vector<>();
            row.add(resultSet.getInt("flight_id"));
            row.add(resultSet.getString("airlines"));
            row.add(resultSet.getString("departure"));
            row.add(resultSet.getString("destination"));
            row.add(resultSet.getTimestamp("departure_time"));
            row.add(resultSet.getTimestamp("arrival_time"));
            row.add(resultSet.getDouble("price"));
            row.add(resultSet.getInt("capacity"));
            row.add(getFlightType(resultSet.getInt("flight_type_id"))); // Add flight type
            flightTableModel.addRow(row);
        }
    }
    private String getFlightType(int flightTypeId) {
        try {
            String query = "SELECT type_name FROM flight_type WHERE flight_type_id = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, flightTypeId);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getString("type_name");
            } else {
                return "Unknown";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return "Unknown";
        }
    }
    private void searchFlights(String destination, String departure, String date) {
        try {
            String query = "SELECT * FROM flight WHERE destination = ? AND departure = ? AND
            DATE(departure_time) = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, destination);
            statement.setString(2, departure);
            statement.setString(3, date);
            ResultSet resultSet = statement.executeQuery();
// Check if there are any flights found
            if (!resultSet.isBeforeFirst()) {
// No flights found
                JOptionPane.showMessageDialog(this, "No flights found for the given criteria.");
            } else {
// Flights found, load them into the table
                loadFlights(resultSet);
            }
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "An error occurred while searching for flights.");
        }
    }
    private void generateBill(int flightId, String departure, String destination, double amountPaid) {
        try {
// Insert bill details into the 'bill' table
            String insertBillQuery = "INSERT INTO bill (customer_id, flight_id, flight_date, departure_airline,
            departure_location, arrival_location, amount_paid, bill_date) VALUES (?, ?, NOW(), ?, ?, ?, ?, NOW())";
            PreparedStatement billStatement = connection.prepareStatement(insertBillQuery,
                    Statement.RETURN_GENERATED_KEYS);
            billStatement.setInt(1, loggedInUserId);
            billStatement.setInt(2, flightId);
            billStatement.setString(3, "Airlines"); // You can set the airline name here
            billStatement.setString(4, departure);
            billStatement.setString(5, destination);
            billStatement.setDouble(6, amountPaid);
            int rowsInserted = billStatement.executeUpdate();
// Get the generated bill ID
            int billId = -1;
            ResultSet generatedKeys = billStatement.getGeneratedKeys();
            if (generatedKeys.next()) {
                billId = generatedKeys.getInt(1);
            }
// If the bill insertion is successful
            if (rowsInserted > 0 && billId != -1) {
// Insert ticket sale details into the 'ticket_sale' table
                String insertTicketQuery = "INSERT INTO ticket_sale (customer_user_id, departure_airline,
                departure_location, departure_time, flight_type, amount_paid) VALUES (?, ?, ?, NOW(), ?, ?)";
                PreparedStatement ticketStatement = connection.prepareStatement(insertTicketQuery);
                ticketStatement.setInt(1, loggedInUserId);
                ticketStatement.setString(2, "Airlines"); // You can set the airline name here
                ticketStatement.setString(3, departure);
                ticketStatement.setString(4, "Domestic"); // You can set the flight type here
                ticketStatement.setDouble(5, amountPaid);
                int ticketRowsInserted = ticketStatement.executeUpdate();
// If ticket sale insertion is successful
                if (ticketRowsInserted > 0) {
                    JOptionPane.showMessageDialog(this, "Flight booked!\nBill ID: " + billId +
                            "\nFrom: " + departure + "\nTo: " + destination + "\nAmount Paid: $" + amountPaid);
                } else {
                    JOptionPane.showMessageDialog(this, "Failed to book the flight. Please try again.");
                }
            } else {
                JOptionPane.showMessageDialog(this, "Failed to generate the bill. Please try again.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "An error occurred while generating the bill.");
        }
    }
    private void postMessage(String message) {
// Implement posting message to chat logic here
// You can append the message to the chatTextArea and store it in the database
// Also append the username before the message
        chatTextArea.append(loggedInUsername + ": " + message + "\n");
        storeFeedback(loggedInUserId, message); // Store the feedback in the database
    }
    private void storeFeedback(int userId, String message) {
        try {
            String query = "INSERT INTO feedback (user_id, message, username) VALUES (?, ?, ?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setInt(1, userId);
            statement.setString(2, message);
            statement.setString(3, loggedInUsername); // Add the username
            int rowsInserted = statement.executeUpdate();
            if (rowsInserted > 0) {
                System.out.println("Feedback stored successfully.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Main();
            }
        });
    }
}
