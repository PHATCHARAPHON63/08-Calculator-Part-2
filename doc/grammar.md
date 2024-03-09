# Grammar for the calculator

## Version 1
The arithmetic expression is only a number.

```
Arithmetic Expression (AE) = Number
```

## Version 2
Add the factorial expression.

```
Arithmetic Expression (AE) = FactExpr
FactExpr = Number {!}

```

## Version 3
Add the power expression.

```
Arithmetic Expression (AE) = PowerExpr
PowerExpr = FactExpr {^ PowerExpr}
FactExpr = Number {!}

```

### Version 4
Add the unary -/+ expression.

```
Arithmetic Expression (AE) = UnaryExpr
UnaryExpr = [- | +] PowerExpr
PowerExpr = FactExpr {^ PowerExpr}
FactExpr = Number {!}

```
