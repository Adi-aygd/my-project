import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class todolist extends JFrame {
    private ArrayList<String> tasks;
    private ArrayList<String> completedTasks;
    private JTextField taskTextField;
    private JList<String> taskList;
    private DefaultListModel<String> listModel;
    private DefaultListModel<String> completedListModel;
    private JProgressBar progressBar;

    public todolist() {
        tasks = new ArrayList<>();
        completedTasks = new ArrayList<>();
        listModel = new DefaultListModel<>();
        completedListModel = new DefaultListModel<>();
        taskList = new JList<>(listModel);

        setTitle("To-Do List App");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel taskPanel = new JPanel();
        taskPanel.setLayout(new BorderLayout());

        JPanel taskComponentsPanel = new JPanel();
        taskComponentsPanel.setBackground(new Color(240, 240, 255));

        taskTextField = new JTextField();
        taskTextField.setFont(new Font("Arial", Font.PLAIN, 14));
        taskTextField.setPreferredSize(new Dimension(250, 30));
        taskTextField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addTask();
            }
        });

        JButton addButton = new JButton("Add Task");
        addButton.setBackground(new Color(50, 205, 50));
        addButton.setForeground(Color.WHITE);
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addTask();
            }
        });

        JButton completeButton = new JButton("Mark as Completed");
        completeButton.setBackground(Color.RED);
        completeButton.setForeground(Color.WHITE);
        completeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                markTaskAsCompleted();
            }
        });

        JButton deleteButton = new JButton("Delete Task");
        deleteButton.setBackground(Color.RED);
        deleteButton.setForeground(Color.WHITE);
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                deleteTask();
            }
        });

        JButton markAllButton = new JButton("Mark All as Completed");
        markAllButton.setBackground(Color.ORANGE);
        markAllButton.setForeground(Color.WHITE);
        markAllButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                markAllAsCompleted();
            }
        });

        progressBar = new JProgressBar();
        progressBar.setStringPainted(true);
        progressBar.setValue(0);

        taskComponentsPanel.add(taskTextField);
        taskComponentsPanel.add(addButton);
        taskComponentsPanel.add(completeButton);
        taskComponentsPanel.add(deleteButton);
        taskComponentsPanel.add(markAllButton);
        taskComponentsPanel.add(progressBar);

        taskPanel.add(taskComponentsPanel, BorderLayout.NORTH);
        taskPanel.add(new JScrollPane(taskList), BorderLayout.CENTER);

        JPanel completedTasksPanel = new JPanel();
        completedTasksPanel.setLayout(new BorderLayout());

        JLabel completedLabel = new JLabel("Completed Tasks:");
        completedLabel.setFont(new Font("Arial", Font.BOLD, 16));
        completedTasksPanel.add(completedLabel, BorderLayout.NORTH);

        JList<String> completedTaskList = new JList<>(completedListModel);
        completedTasksPanel.add(new JScrollPane(completedTaskList), BorderLayout.CENTER);

        JSplitPane splitPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT, taskPanel, completedTasksPanel);
        add(splitPane);

        setVisible(true);
    }

    private void updateProgressBar() {
        int totalTasks = tasks.size() + completedTasks.size();
        int completedTasksCount = completedTasks.size();
        int percentage = (int) (((double) completedTasksCount / totalTasks) * 100);
        progressBar.setValue(percentage);
    }

    private void addTask() {
        String task = taskTextField.getText().trim();
        if (!task.isEmpty()) {
            tasks.add(task);
            listModel.addElement(task);
            taskTextField.setText("");
            updateProgressBar();
        }
    }

    private void markTaskAsCompleted() {
        int selectedIndex = taskList.getSelectedIndex();
        if (selectedIndex != -1) {
            String completedTask = tasks.get(selectedIndex);
            completedTasks.add(completedTask);
            completedListModel.addElement(completedTask);
            listModel.remove(selectedIndex);
            tasks.remove(selectedIndex);
            updateProgressBar();
        }
    }

    private void deleteTask() {
        int selectedIndex = taskList.getSelectedIndex();
        if (selectedIndex != -1) {
            listModel.remove(selectedIndex);
            tasks.remove(selectedIndex);
            updateProgressBar();
        }
    }

    private void markAllAsCompleted() {
        for (String task : tasks) {
            completedTasks.add(task);
            completedListModel.addElement(task);
        }
        tasks.clear();
        listModel.removeAllElements();
        updateProgressBar();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new todolist();
            }
        });
    }
}