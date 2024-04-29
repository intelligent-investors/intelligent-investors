import React, { useState } from 'react';

export default function Cashflow() {
  const people = [
    { name: "Tiana", role: "Teacher", salary: 3300 },
    { name: "David", role: "Doctor", salary: 13200 },
    { name: "Eric", role: "Engineer", salary: 4500 },
    { name: "Jenifer", role: "Janitor", salary: 1600 },
    { name: "Levi", role: "Lawyer", salary: 7500 },
  ];

  // Function to select a random person from the people array
  const getRandomPerson = (people) => {
    return people[Math.floor(Math.random() * people.length)];
  };

  // Use useState to manage the random person's state
  const [person, setPerson] = useState(() => getRandomPerson(people));

  // Function to update the person state to a new random person
  const handleChangePerson = () => {
    let newPerson;
    do {
      newPerson = getRandomPerson(people);
    } while (newPerson.name === person.name); // Keep selecting until a different person is found
    setPerson(newPerson);
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <b>Cashflow Example</b>
      <table style={{ margin: 'auto', borderCollapse: 'collapse', display: 'flex', justifyContent: 'center' }}>
        <tbody>
          <tr>
            <th style={{ border: '1px solid black', padding: '8px' }}>Name</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>Profession</th>
            <th style={{ border: '1px solid black', padding: '8px' }}>Salary</th>
          </tr>
          <tr>
            <td style={{ border: '1px solid black', padding: '8px' }}>{person.name}</td>
            <td style={{ border: '1px solid black', padding: '8px' }}>{person.role}</td>
            <td style={{ border: '1px solid black', padding: '8px', color: 'red' }}>${person.salary.toLocaleString()}</td>
          </tr>
        </tbody>
      </table>
      <button onClick={handleChangePerson}>Change Person</button>
    </div>
  );
}