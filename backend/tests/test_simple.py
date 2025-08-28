def test_simple():
    """Simple test to verify pytest is working."""
    assert 1 + 1 == 2

def test_import():
    """Test that we can import from api_server."""
    import os
    import sys
    
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)
    print("Contents of current directory:", os.listdir('.'))
    
    try:
        import api_server
        print("api_server imported successfully")
        print("api_server location:", api_server.__file__)
        
        from api_server.core.log import get_logger
        assert get_logger is not None
        print("Successfully imported get_logger")
    except ImportError as e:
        print(f"Import error details: {e}")
        assert False, f"Failed to import: {e}"