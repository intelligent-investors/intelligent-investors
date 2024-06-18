// Import necessary modules from Jest and @testing-library/react
import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import Quiz from './Quiz.js'; // Adjust path as needed

// Describe the tests for the Quiz component
describe('Quiz Component', () => {
  let questions;

  beforeEach(() => {
    // Define mock questions for testing
    questions = [
      {
        question: 'What is 2 + 2?',
        answer: [
          { value: '3', correct: 'false', explanation: 'Incorrect, try again.' },
          { value: '4', correct: 'true', explanation: 'Correct answer!' },
          { value: '5', correct: 'false', explanation: 'Incorrect, try again.' },
        ],
      },
      // Add more mock questions as needed
    ];
  });

  // Test case: Renders the Quiz component
  it('should render the Quiz component', () => {
    render(<Quiz questions={questions} />);
    
    // Example assertion: Check if the Quiz component renders correctly
    expect(screen.getByText(/Quiz/i)).toBeInTheDocument();
  });

  // Example of more test cases:
  it('should display questions and options', () => {
    render(<Quiz questions={questions} />);

    // Example assertion: Check if the first question is rendered
    expect(screen.getByText('What is 2 + 2?')).toBeInTheDocument();

    // Example assertion: Check if the options are rendered
    expect(screen.getByText('3')).toBeInTheDocument();
    expect(screen.getByText('4')).toBeInTheDocument();
    expect(screen.getByText('5')).toBeInTheDocument();
  });

  it('should allow selecting an answer and submitting', () => {
    render(<Quiz questions={questions} />);

    // Example interaction: Select an answer and submit
    fireEvent.click(screen.getByLabelText('4')); // Select the correct answer '4'
    fireEvent.click(screen.getByText('Submit')); // Click the Submit button

    // Example assertion: Check if the correct/incorrect message is displayed
    expect(screen.getByText('Correct!')).toBeInTheDocument();
  });
});