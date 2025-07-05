import React, { useState, useEffect } from 'react';
import { ReactCompareSlider, ReactCompareSliderImage } from 'react-compare-slider';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [originalImage, setOriginalImage] = useState(null);
  const [enhancedImage, setEnhancedImage] = useState(null);
  const [error, setError] = useState(null);
  const [enhancing, setEnhancing] = useState(false);
  const [theme, setTheme] = useState('dark');

  useEffect(() => {
    document.body.className = theme;
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prevTheme => (prevTheme === 'light' ? 'dark' : 'light'));
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setSelectedFile(file);
      setOriginalImage(URL.createObjectURL(file));
      setEnhancedImage(null);
      setError(null);
    }
  };

  const handleEnhanceClick = async () => {
    if (!selectedFile) {
      setError('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('photo', selectedFile);

    setEnhancing(true);
    setError(null);

    try {
                        const response = await fetch('https://ai-photo-enhancer-backend.onrender.com/enhance', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const imageBlob = await response.blob();
      const imageUrl = URL.createObjectURL(imageBlob);
      setEnhancedImage(imageUrl);
    } catch (err) {
      setError(err.message);
    } finally {
      setEnhancing(false);
    }
  };

  return (
    <div className={`app-container ${theme}`}>
        <button onClick={toggleTheme} className="theme-switcher">
            {theme === 'light' ? '🌙' : '☀️'}
        </button>
      <div className="controls-panel">
        <div className="header">
          <h1>AI Photo Enhancer</h1>
          <p>Restore and upscale your images with a single click.</p>
        </div>

        <div className="upload-btn-wrapper">
          <button className="btn">Choose a Photo</button>
          <input type="file" onChange={handleFileChange} accept="image/*" />
        </div>

        {selectedFile && (
            <div className='file-info'>
                <p>{selectedFile.name}</p>
            </div>
        )}

        {originalImage && (
            <button onClick={handleEnhanceClick} disabled={enhancing} className='btn'>
                {enhancing ? 'Enhancing...' : 'Enhance Photo'}
            </button>
        )}

        {enhancing && <div className="loader"></div>}
        {error && <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>}
      </div>

      <div className="image-panel">
        {originalImage && enhancedImage ? (
          <ReactCompareSlider
            itemOne={<ReactCompareSliderImage src={originalImage} alt="Original" />}
            itemTwo={<ReactCompareSliderImage src={enhancedImage} alt="Enhanced" />}
            style={{ width: '100%', height: '100%' }}
          />
        ) : originalImage ? (
            <img src={originalImage} alt="Original" className='image-display'/>
        ) : (
          <div className="placeholder">
            <div className="placeholder-icon">🖼️</div>
            <h2>Your enhanced image will appear here</h2>
            <p>Upload a photo to get started</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
