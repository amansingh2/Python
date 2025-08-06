# Composition Over Inheritance – Key Points


---

## Key Idea
- Favor **composition** (using objects as building blocks) over **inheritance** (extending from base classes).
- This approach improves **flexibility**, **modularity**, and **maintainability**.

---

## Problem: The Subclass Explosion

1. **Too Many Subclasses**
   - Supporting combinations of behaviors (e.g., `Flying`, `Swimming`, `Walking`) via inheritance leads to a **combinatorial explosion**:
     ```
     FlyingSwimmingCreature
     SwimmingWalkingCreature
     FlyingWalkingCreature
     ...
     ```
   - For `n` behaviors, you may need up to `2^n` subclasses.

2. **Rigid Design**
   - Inheritance **locks behavior at compile time**.
   - Changing behavior requires altering or creating new subclasses.
   - Violates **Open/Closed Principle**: classes aren’t open for extension without modification.

---

## Solution: Use Composition

1. **Behavior as Components**
   - Encapsulate behaviors into small, focused classes (e.g., `Flyer`, `Swimmer`).
   - Inject them into other objects via composition.

2. **Example**
   ```
   class Creature:
       def __init__(self, fly_behavior, swim_behavior):
           self.fly = fly_behavior
           self.swim = swim_behavior
