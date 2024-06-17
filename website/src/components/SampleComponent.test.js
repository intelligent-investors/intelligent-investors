import React from 'react';
import { render, screen } from '@testing-library/react';
import SampleComponent from './SampleComponent';

describe('SampleComponent', () => {
  test('renders the heading and paragraph', () => {
    render(<SampleComponent />);
    
    // Check if the heading is rendered
    const headingElement = screen.getByText(/Hello, world!/i);
    expect(headingElement).toBeInTheDocument();

    // Check if the paragraph is rendered
    const paragraphElement = screen.getByText(/This is a simple React component./i);
    expect(paragraphElement).toBeInTheDocument();
  });
});