import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import Quiz from './Quiz.js';

describe('Quiz Component', () => {
  let questions;

  beforeEach(() => {
    questions = [
      {
        question: 'What is 2 + 2?',
        answer: [
          { value: '3', correct: 'false', explanation: 'Incorrect, try again.' },
          { value: '4', correct: 'true', explanation: '4 is the correct answer!' },
          { value: '5', correct: 'false'},
        ],
      }
    ];
  });

  it('should render the Quiz component', () => {
    render(<Quiz questions={questions} />);
    
    expect(screen.getByText(/Quiz/i)).toBeInTheDocument();
  });

  it('should display questions and options', () => {
    render(<Quiz questions={questions} />);

    expect(screen.getByText(/What is 2 \+ 2\?/)).toBeInTheDocument();
    expect(screen.getByText(/A. 3/)).toBeInTheDocument();
    expect(screen.getByText(/B. 4/)).toBeInTheDocument();
    expect(screen.getByText(/C. 5/)).toBeInTheDocument();
  });

  it('should display correct result', () => {
    render(<Quiz questions={questions} />);

    fireEvent.click(screen.getByLabelText(/B. 4/));
    fireEvent.click(screen.getByText('Submit')); 

    expect(screen.getByText(/Correct!/)).toBeInTheDocument();
    expect(screen.getByText(/4 is the correct answer!/)).toBeInTheDocument();
  });

  it('should display result when no answer is chosen', () => {
    render(<Quiz questions={questions} />);

    fireEvent.click(screen.getByText('Submit')); 

    expect(screen.getByText(/Incorrect. The correct answer is 4/)).toBeInTheDocument();
  });

  it('should display explanation on wrong answer', () => {
    render(<Quiz questions={questions} />);

    fireEvent.click(screen.getByLabelText(/A. 3/));
    fireEvent.click(screen.getByText('Submit')); 

    expect(screen.getByText(/Incorrect. The correct answer is 4/)).toBeInTheDocument();
    expect(screen.getByText(/4 is the correct answer!/)).toBeInTheDocument();
  });
});