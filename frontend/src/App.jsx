import './index.css'
import './App.css'
import logo from './assets/react.svg'

function App() {

  return (
    <>
    <nav className='navbar'>
      <div className="container">
        <div className="logo">
          <a href="index.html">
            <img src={logo} alt="logo"/>
          </a>
        </div>
        <div className='header'>
          <a href="index.html">
            <h2 className='text-xl'>Simple Neural Search</h2>
          </a>
        </div>
      </div>
    </nav>
    <section className="hero">
      <div className="container">
        <div className="hero-item hero-input">
          <h3 className='text-md'>Configuration</h3>
          <h4 className='text-sm'> Say something about job description </h4>
          <form action="#">
            <textarea name="user-query"></textarea>
            <br />
            <input className='btn' type="submit" value="submit" />
          </form>
        </div>
        <div className="hero-item hero-output">
          <h3 className='text-md'>Job Openings</h3>
          <textarea name="query-result" ></textarea>
        </div>
      </div>
    </section>
    </>
  )
}

export default App
