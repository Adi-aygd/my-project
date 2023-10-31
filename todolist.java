import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class todolist extends JFrame {
    private ArrayList<String> tasks;
    private JTextField taskTextField;
    private JList<String> taskList;
    private DefaultListModel<String> listModel;

    private JTextField expressionTextField;
    private JLabel resultLabel;

    public CombinedApp() {
        // Initialize the tasks list and the JFrame
        tasks = new ArrayList<>();
        listModel = new DefaultListModel<>();
        taskList = new JList<>(listModel);

        // Set up the JFrame
        setTitle("Combined App");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a JTabbedPane to hold the two panels
        JTabbedPane tabbedPane = new JTabbedPane();

        // Create the To-Do List panel
        JPanel todoPanel = new JPanel();
        todoPanel.setLayout(new BorderLayout());

        // Create a JTextField for entering tasks
        taskTextField = new JTextField();

        // Create a JButton to add tasks
        JButton addButton = new JButton("Add Task");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String task = taskTextField.getText().trim();
                if (!task.isEmpty()) {
                    tasks.add(task);
                    listModel.addElement(task);
                    taskTextField.setText("");
                }
            }
        });

        // Create a JButton to delete tasks
        JButton deleteButton = new JButton("Delete Task");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int selectedIndex = taskList.getSelectedIndex();
                if (selectedIndex != -1) {
                    tasks.remove(selectedIndex);
                    listModel.remove(selectedIndex);
                }
            }
        });

        // Add components to the todoPanel
        todoPanel.add(taskTextField, BorderLayout.NORTH);
        todoPanel.add(new JScrollPane(taskList), BorderLayout.CENTER);
        todoPanel.add(addButton, BorderLayout.WEST);
        todoPanel.add(deleteButton, BorderLayout.EAST);

        // Create the Calculator panel
        JPanel calculatorPanel = new JPanel();
        calculatorPanel.setLayout(new BorderLayout());

        // Create a JTextField for entering expressions
        expressionTextField = new JTextField();

        // Create a JButton to calculate the expression
        JButton calculateButton = new JButton("Calculate");
        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String expression = expressionTextField.getText();
                try {
                    double result = evaluateExpression(expression);
                    resultLabel.setText("Result: " + result);
                } catch (Exception ex) {
                    resultLabel.setText("Invalid expression");
                }
            }
        });

        // Create a JLabel to display the result
        resultLabel = new JLabel("Result: ");

        // Add components to the calculatorPanel
        calculatorPanel.add(expressionTextField, BorderLayout.NORTH);
        calculatorPanel.add(calculateButton, BorderLayout.CENTER);
        calculatorPanel.add(resultLabel, BorderLayout.SOUTH);

        // Add the panels to the tabbedPane
        tabbedPane.addTab("To-Do List", todoPanel);
        tabbedPane.addTab("Calculator", calculatorPanel);

        // Add the tabbedPane to the JFrame
        add(tabbedPane);

        // Display the JFrame
        setVisible(true);
    }

    private double evaluateExpression(String expression) {
        // Implement your expression evaluation logic here
        // For simplicity, let's just return 0 for now
        return 0;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new CombinedApp();
            }
        });
    }
}
