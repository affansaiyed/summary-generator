import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

var apiEndpoint = 'http://localhost:5000/api';

async function handleSubmit(_event, jobTitle, company, qualis, workExp, setResponse) {
  const response = await fetch(apiEndpoint, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify({ jobTitle, company, qualis, workExp })
  });

  const output = await response.json();
  setResponse(JSON.stringify(output));

}

function App() {
  const [jobTitle, setJobTitle] = useState(null);
  const [company, setCompany] = useState(null);
  const [qualis, setQualis] = useState(null);
  const [workExp, setWorkExp] = useState(null);

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
      </form>
      <input type = "submit" value = "Submit" />
      <div className="OutputArea">
        <label className='Output'> Output:
          <textarea value = {response} readOnly></textarea>
        </label>
      </div>
    </div>
  );
}

export default App;
