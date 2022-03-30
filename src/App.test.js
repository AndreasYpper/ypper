import { render, screen } from '@testing-library/react';
import App from './App';

test('Renders Hi!', () => {
  render(<App />);
  const linkElement = screen.getByText(/Hi! I'm Andreas Ypper/i);
  expect(linkElement).toBeInTheDocument();
});
