"""
Test script for Technical ATS Resume Expert
This script tests various components of the application.
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

def test_imports():
    """Test if all modules can be imported successfully."""
    print("🧪 Testing module imports...")
    
    try:
        from src.config import Config
        print("✅ Config module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Config: {e}")
        return False
    
    try:
        from src.utils import PDFProcessor, TextAnalyzer
        print("✅ Utils module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Utils: {e}")
        return False
    
    try:
        from src.ai_service import GeminiService, PromptManager
        print("✅ AI Service module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import AI Service: {e}")
        return False
    
    try:
        from src.visualization import ChartGenerator, UIComponents
        print("✅ Visualization module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Visualization: {e}")
        return False
    
    return True

def test_dependencies():
    """Test if all required dependencies are available."""
    print("\n🧪 Testing dependencies...")
    
    dependencies = [
        'streamlit',
        'google.generativeai',
        'matplotlib',
        'fitz',
        'PIL',
        'dotenv'
    ]
    
    all_good = True
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} is available")
        except ImportError as e:
            print(f"❌ {dep} is missing: {e}")
            all_good = False
    
    return all_good

def test_config():
    """Test configuration management."""
    print("\n🧪 Testing configuration...")
    
    try:
        from src.config import Config
        
        # Test config attributes
        assert hasattr(Config, 'GEMINI_MODEL'), "GEMINI_MODEL not found"
        assert hasattr(Config, 'APP_TITLE'), "APP_TITLE not found"
        assert hasattr(Config, 'MAX_FILE_SIZE'), "MAX_FILE_SIZE not found"
        
        print("✅ Configuration attributes are correct")
        
        # Test methods
        assert hasattr(Config, 'validate_config'), "validate_config method not found"
        assert hasattr(Config, 'setup_logging'), "setup_logging method not found"
        
        print("✅ Configuration methods are available")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_utilities():
    """Test utility functions."""
    print("\n🧪 Testing utilities...")
    
    try:
        from src.utils import PDFProcessor, TextAnalyzer
        
        # Test PDFProcessor methods
        processor = PDFProcessor()
        assert hasattr(processor, 'validate_pdf_file'), "validate_pdf_file method not found"
        assert hasattr(processor, 'process_pdf'), "process_pdf method not found"
        
        print("✅ PDFProcessor methods are available")
        
        # Test TextAnalyzer methods
        analyzer = TextAnalyzer()
        assert hasattr(analyzer, 'extract_match_percentage'), "extract_match_percentage method not found"
        assert hasattr(analyzer, 'validate_job_description'), "validate_job_description method not found"
        
        print("✅ TextAnalyzer methods are available")
        
        # Test percentage extraction with sample text
        sample_text = "Match Percentage: 85%"
        percentage = analyzer.extract_match_percentage(sample_text)
        assert percentage == 85, f"Expected 85, got {percentage}"
        
        print("✅ Percentage extraction works correctly")
        
        return True
        
    except Exception as e:
        print(f"❌ Utilities test failed: {e}")
        return False

def test_prompts():
    """Test prompt management."""
    print("\n🧪 Testing prompt management...")
    
    try:
        from src.ai_service import PromptManager
        
        # Test prompt retrieval
        analysis_prompt = PromptManager.get_prompt('analysis')
        improvement_prompt = PromptManager.get_prompt('improvement')
        matching_prompt = PromptManager.get_prompt('matching')
        
        assert isinstance(analysis_prompt, str), "Analysis prompt is not a string"
        assert isinstance(improvement_prompt, str), "Improvement prompt is not a string"
        assert isinstance(matching_prompt, str), "Matching prompt is not a string"
        
        assert len(analysis_prompt) > 100, "Analysis prompt is too short"
        assert len(improvement_prompt) > 100, "Improvement prompt is too short"
        assert len(matching_prompt) > 100, "Matching prompt is too short"
        
        print("✅ All prompts are available and valid")
        
        return True
        
    except Exception as e:
        print(f"❌ Prompt management test failed: {e}")
        return False

def test_visualization():
    """Test visualization components."""
    print("\n🧪 Testing visualization...")
    
    try:
        from src.visualization import ChartGenerator, UIComponents
        
        # Test ChartGenerator methods
        chart_gen = ChartGenerator()
        assert hasattr(chart_gen, 'create_match_pie_chart'), "create_match_pie_chart method not found"
        
        print("✅ ChartGenerator methods are available")
        
        # Test UIComponents methods
        ui = UIComponents()
        assert hasattr(ui, 'display_success_message'), "display_success_message method not found"
        assert hasattr(ui, 'display_error_message'), "display_error_message method not found"
        
        print("✅ UIComponents methods are available")
        
        return True
        
    except Exception as e:
        print(f"❌ Visualization test failed: {e}")
        return False

def test_file_structure():
    """Test if required files and directories exist."""
    print("\n🧪 Testing file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'README.md',
        'LICENSE',
        '.env.example',
        '.gitignore',
        'src/__init__.py',
        'src/config.py',
        'src/utils.py',
        'src/ai_service.py',
        'src/visualization.py'
    ]
    
    required_dirs = [
        'src',
        'logs',
        'docs',
        'assets'
    ]
    
    all_good = True
    
    # Check files
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} is missing")
            all_good = False
    
    # Check directories
    for dir in required_dirs:
        if os.path.isdir(dir):
            print(f"✅ {dir}/ directory exists")
        else:
            print(f"❌ {dir}/ directory is missing")
            all_good = False
    
    return all_good

def main():
    """Run all tests."""
    print("🚀 Starting Technical ATS Resume Expert Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_dependencies,
        test_file_structure,
        test_config,
        test_utilities,
        test_prompts,
        test_visualization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print(f"❌ {test.__name__} failed")
        except Exception as e:
            print(f"❌ {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\n🚀 To start the application, run:")
        print("   streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues before running the application.")
    
    return passed == total

if __name__ == "__main__":
    main()
