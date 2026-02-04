
from src.Student_Grade_Calculator import Calculate_grade

def test_grade_aplus():
    # Average 93 -> A+
    assert Calculate_grade([90, 95, 92, 98, 90]) == "A+"

def test_grade_a():
    # Average 85 -> A
    assert Calculate_grade([85, 85, 85, 85, 85]) == "A"

def test_grade_b_plus():
    # Average 77 -> B+
    assert Calculate_grade([75, 80, 75, 75, 80]) == "B+"

def test_grade_b():
    # Average 62 -> B
    assert Calculate_grade([60, 65, 60, 62, 63]) == "B"

def test_grade_c():
    # Average 51.6 -> C
    assert Calculate_grade([50, 52, 55, 50, 51]) == "C"

def test_grade_d():
    # Average 45 -> D
    assert Calculate_grade([45, 45, 45, 45, 45]) == "D"

def test_grade_fail():
    # Average 29 -> Fail
    assert Calculate_grade([40, 30, 45, 20, 10]) == "Fail"

def test_empty_input():
    assert Calculate_grade([]) == "No marks provided"

def test_invalid_marks():
    assert Calculate_grade([110, 90, 80, 70, 60]) == "Invalid marks detected"
    assert Calculate_grade([-5, 50, 60, 70, 80]) == "Invalid marks detected"