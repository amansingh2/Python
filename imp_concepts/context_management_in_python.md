# Context Manager!
- it's an special kind of object that knows how to manage resources , it has two key methods
  enter and exit 

```
class ContextManager:
    def __enter__(self):  
        print("Entering Context!")
        return "Some resources!"
        
    def __exit__(self , exc_type , exc_value , traceback):
        print("Exiting Context")
        
with ContextManager() as cm
    print(f"using : {cm}")
```

- enter() -> handles the setup!
- exit() -> takes care of the clean-up!