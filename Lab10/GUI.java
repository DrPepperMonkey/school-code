package Lab10;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI {
    private JFrame frame;
    public GUI() {
        frame = new JFrame();
        frame.setSize(600, 900);
        JPanel main = new JPanel(new GridBagLayout());
        main.setLayout(new BoxLayout(main, BoxLayout.Y_AXIS));
        frame.add(main);
        JPanel topPanel = new JPanel();
        topPanel.add(new JTextArea());
        main.add(topPanel);
        JPanel bottomPanel = new JPanel(new GridBagLayout());
        GridBagConstraints c = new GridBagConstraints();
        c.gridheight = 1;
        c.gridwidth = 1;
        c.anchor = GridBagConstraints.FIRST_LINE_START;
        c.fill = GridBagConstraints.BOTH;
        JPanel numbers = new JPanel(new GridLayout(3,3));
        for (int i = 1; i < 10; i++) {
            String count = Integer.toString(i);
            JButton tmp = new JButton(Integer.toString(i));
            numbers.add(tmp);
            tmp.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    System.out.print(count);
                }
            });
        }
        c.weightx = 1;
        c.weighty = 0.75;
        bottomPanel.add(numbers);
        JButton plus = new JButton("+");
        plus.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.print(" + ");
            }
        });
        JButton minus = new JButton("-");
        minus.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.print(" - ");
            }
        });
        JButton div = new JButton("/");
        div.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.print(" / ");
            }
        });
        JButton multi = new JButton("*");
        multi.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.print(" * ");
            }
        });


        main.add(bottomPanel);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
