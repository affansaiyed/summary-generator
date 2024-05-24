import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

var apiEndpoint = 'http://localhost:5000/api'; //placeholder

function App() {
  const [jobTitle, setJobTitle] = useState('');
  const [company, setCompany] = useState('');
  const [qualis, setQualis] = useState('');
  const [workExp, setWorkExp] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (event) => { 
    event.preventDefault();
    let body_string = `Job Title: ${jobTitle}, Preferred Qualifications: ${qualis}, Hiring Company: ${company}, Past Work Experience: ${workExp}`
    const encodedJobInfo = encodeURIComponent(body_string);
    const req = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-type': 'application/x-www-form-urlencoded',
      },
      body: `$info=${encodedJobInfo}`
    });
    if (!response.ok) throw new Error(`HTTP error status: ${response.status}`);
    const output = await req.json();
    
    setResponse(output);
  
  }

  return (
    <div className="Form">
      <form onSubmit={(event) => handleSubmit(event, jobTitle, company, qualis, workExp)}>
        <label> Company: 
          <input type = "text" value = {company} onChange={e=>setCompany(e.target.value)} />
        </label>
        <label> Job Title: 
          <input type = "text" value = {jobTitle} onChange={e=>setJobTitle(e.target.value)} />
        </label>
        <label> Qualifications: 
          <input type = "text" value = {qualis} onChange={e=>setQualis(e.target.value)} />
        </label>
        <label> Work History: 
          <input type = "text" value = {workExp} onChange={e=>setWorkExp(e.target.value)} />
        </label>
        <button type = "submit">Submit</button>
      </form>
      {response && <p> Output: {JSON.stringify(response)}</p>}
    </div>
  );
}

export default App;
