"""
Test precedences
"""

try:
    from test.mathics_helper import check_evaluation, evaluate, session

    MATHICS_NOT_INSTALLED = False
except ModuleNotFoundError:
    MATHICS_NOT_INSTALLED = True

import pytest

WMA_PRECEDENCES = {
    "CompoundExpression": 10.0,
    "Put": 30.0,
    "PutAppend": 30.0,
    "Set": 40.0,
    "SetDelayed": 40.0,
    "UpSet": 40.0,
    "UpSetDelayed": 40.0,
    "Because": 50.0,
    "Therefore": 50.0,
    "Postfix": 70.0,
    "Colon": 80.0,
    "Function": 90.0,
    "AddTo": 100.0,
    "DivideBy": 100.0,
    "SubtractFrom": 100.0,
    "TimesBy": 100.0,
    "ReplaceAll": 110.0,
    "ReplaceRepeated": 110.0,
    "RuleDelayed": 120.0,
    "Rule": 120.0,
    "Condition": 130.0,
    "StringExpression": 135.0,
    "Optional": 140.0,
    "Alternatives": 160.0,
    "Repeated": 170.0,
    "RepeatedNull": 170.0,
    "SuchThat": 180.0,
    "DoubleLeftTee": 190.0,
    "DoubleRightTee": 190.0,
    "DownTee": 190.0,
    "LeftTee": 190.0,
    "Perpendicular": 190.0,
    "RightTee": 190.0,
    "UpTee": 190.0,
    "Implies": 200.0,
    "Equivalent": 205.0,
    "And": 215.0,
    "Nand": 215.0,
    "Nor": 215.0,
    "Or": 215.0,
    "Xor": 215.0,
    "Not": 230.0,
    "RoundImplies": 240.0,
    "NotReverseElement": 250.0,
    "NotSquareSubsetEqual": 250.0,
    "NotSquareSupersetEqual": 250.0,
    "NotSubset": 250.0,
    "NotSubsetEqual": 250.0,
    "NotSuperset": 250.0,
    "NotSupersetEqual": 250.0,
    "ReverseElement": 250.0,
    "SquareSubset": 250.0,
    "SquareSubsetEqual": 250.0,
    "SquareSuperset": 250.0,
    "SquareSupersetEqual": 250.0,
    "Subset": 250.0,
    "SubsetEqual": 250.0,
    "Superset": 250.0,
    "SupersetEqual": 250.0,
    "DoubleLeftArrow": 270.0,
    "DoubleLeftRightArrow": 270.0,
    "DoubleRightArrow": 270.0,
    "DownLeftRightVector": 270.0,
    "DownLeftTeeVector": 270.0,
    "DownLeftVector": 270.0,
    "DownLeftVectorBar": 270.0,
    "DownRightTeeVector": 270.0,
    "DownRightVector": 270.0,
    "DownRightVectorBar": 270.0,
    "LeftArrow": 270.0,
    "LeftArrowBar": 270.0,
    "LeftArrowRightArrow": 270.0,
    "LeftRightArrow": 270.0,
    "LeftRightVector": 270.0,
    "LeftTeeArrow": 270.0,
    "LeftTeeVector": 270.0,
    "LeftVector": 270.0,
    "LeftVectorBar": 270.0,
    "LowerLeftArrow": 270.0,
    "LowerRightArrow": 270.0,
    "RightArrow": 270.0,
    "RightArrowBar": 270.0,
    "RightArrowLeftArrow": 270.0,
    "RightTeeArrow": 270.0,
    "RightTeeVector": 270.0,
    "RightVector": 270.0,
    "RightVectorBar": 270.0,
    "ShortLeftArrow": 270.0,
    "ShortRightArrow": 270.0,
    "UpperLeftArrow": 270.0,
    "UpperRightArrow": 270.0,
    "DoubleVerticalBar": 280.0,
    "NotDoubleVerticalBar": 280.0,
    "VerticalBar": 280.0,
    "Equal": 290.0,
    "Greater": 290.0,
    "GreaterEqual": 290.0,
    "Less": 290.0,
    "LessEqual": 290.0,
    "SameQ": 290.0,
    "Unequal": 290.0,
    "UnsameQ": 290.0,
    "Congruent": 290.0,
    "CupCap": 290.0,
    "DotEqual": 290.0,
    "EqualTilde": 290.0,
    "Equilibrium": 290.0,
    "GreaterEqualLess": 290.0,
    "GreaterFullEqual": 290.0,
    "GreaterGreater": 290.0,
    "GreaterLess": 290.0,
    "GreaterTilde": 290.0,
    "HumpDownHump": 290.0,
    "HumpEqual": 290.0,
    "LeftTriangle": 290.0,
    "LeftTriangleBar": 290.0,
    "LeftTriangleEqual": 290.0,
    "LessEqualGreater": 290.0,
    "LessFullEqual": 290.0,
    "LessGreater": 290.0,
    "LessLess": 290.0,
    "LessTilde": 290.0,
    "NestedGreaterGreater": 290.0,
    "NestedLessLess": 290.0,
    "NotCongruent": 290.0,
    "NotCupCap": 290.0,
    "NotGreater": 290.0,
    "NotGreaterEqual": 290.0,
    "NotGreaterFullEqual": 290.0,
    "NotGreaterLess": 290.0,
    "NotGreaterTilde": 290.0,
    "NotLeftTriangle": 290.0,
    "NotLeftTriangleEqual": 290.0,
    "NotLess": 290.0,
    "NotLessEqual": 290.0,
    "NotLessFullEqual": 290.0,
    "NotLessGreater": 290.0,
    "NotLessTilde": 290.0,
    "NotPrecedes": 290.0,
    "NotPrecedesSlantEqual": 290.0,
    "NotPrecedesTilde": 290.0,
    "NotRightTriangle": 290.0,
    "NotRightTriangleEqual": 290.0,
    "NotSucceeds": 290.0,
    "NotSucceedsSlantEqual": 290.0,
    "NotSucceedsTilde": 290.0,
    "NotTilde": 290.0,
    "NotTildeEqual": 290.0,
    "NotTildeFullEqual": 290.0,
    "NotTildeTilde": 290.0,
    "Precedes": 290.0,
    "PrecedesEqual": 290.0,
    "PrecedesSlantEqual": 290.0,
    "PrecedesTilde": 290.0,
    "Proportion": 290.0,
    "Proportional": 290.0,
    "ReverseEquilibrium": 290.0,
    "RightTriangle": 290.0,
    "RightTriangleBar": 290.0,
    "RightTriangleEqual": 290.0,
    "Succeeds": 290.0,
    "SucceedsEqual": 290.0,
    "SucceedsSlantEqual": 290.0,
    "SucceedsTilde": 290.0,
    "Tilde": 290.0,
    "TildeEqual": 290.0,
    "TildeFullEqual": 290.0,
    "TildeTilde": 290.0,
    "DirectedEdge": 295.0,
    "UndirectedEdge": 295.0,
    "SquareUnion": 300.0,
    "UnionPlus": 300.0,
    "Span": 305.0,
    "SquareIntersection": 305.0,
    "MinusPlus": 310.0,
    "PlusMinus": 310.0,
    "Plus": 310.0,
    "Subtract": 310.0,
    "CircleMinus": 330.0,
    "CirclePlus": 330.0,
    "Cup": 340.0,
    "Cap": 350.0,
    "Coproduct": 360.0,
    "VerticalTilde": 370.0,
    "Star": 390.0,
    "Times": 400.0,
    "CenterDot": 410.0,
    "CircleTimes": 420.0,
    "Vee": 430.0,
    "Wedge": 440.0,
    "Diamond": 450.0,
    "Backslash": 460.0,
    "Divide": 470.0,
    "Minus": 480.0,
    "Dot": 490.0,
    "CircleDot": 520.0,
    "SmallCircle": 530.0,
    "Square": 540.0,
    "CapitalDifferentialD": 550.0,
    "Del": 550.0,
    "DifferentialD": 550.0,
    "DoubleDownArrow": 580.0,
    "DoubleLongLeftArrow": 580.0,
    "DoubleLongLeftRightArrow": 580.0,
    "DoubleLongRightArrow": 580.0,
    "DoubleUpArrow": 580.0,
    "DoubleUpDownArrow": 580.0,
    "DownArrow": 580.0,
    "DownArrowBar": 580.0,
    "DownArrowUpArrow": 580.0,
    "DownTeeArrow": 580.0,
    "LeftDownTeeVector": 580.0,
    "LeftDownVector": 580.0,
    "LeftDownVectorBar": 580.0,
    "LeftUpDownVector": 580.0,
    "LeftUpTeeVector": 580.0,
    "LeftUpVector": 580.0,
    "LeftUpVectorBar": 580.0,
    "LongLeftArrow": 580.0,
    "LongLeftRightArrow": 580.0,
    "LongRightArrow": 580.0,
    "ReverseUpEquilibrium": 580.0,
    "RightDownTeeVector": 580.0,
    "RightDownVector": 580.0,
    "RightDownVectorBar": 580.0,
    "RightUpDownVector": 580.0,
    "RightUpTeeVector": 580.0,
    "RightUpVector": 580.0,
    "RightUpVectorBar": 580.0,
    "ShortDownArrow": 580.0,
    "ShortUpArrow": 580.0,
    "UpArrow": 580.0,
    "UpArrowBar": 580.0,
    "UpArrowDownArrow": 580.0,
    "UpDownArrow": 580.0,
    "UpEquilibrium": 580.0,
    "UpTeeArrow": 580.0,
    "Power": 590.0,
    "StringJoin": 600.0,
    "Factorial": 610.0,
    "Factorial2": 610.0,
    "Apply": 620.0,
    "Map": 620.0,
    "Prefix": 640.0,
    "Decrement": 660.0,
    "Increment": 660.0,
    "PreDecrement": 660.0,
    "PreIncrement": 660.0,
    "Unset": 670.0,
    "Information": 670.0,
    "GreaterSlantEqual": 670.0,
    "LessSlantEqual": 670.0,
    "Derivative": 670.0,
    "MapApply": 670.0,
    "PatternTest": 680.0,
    "Get": 720.0,
    "MessageName": 750.0,
}

SORTED_SYMBOLS_BY_PRECEDENCE = [
    "CompoundExpression",
    "Put",
    "PutAppend",
    "Set",
    "SetDelayed",
    "UpSet",
    "UpSetDelayed",
    "Because",
    "Therefore",
    "Postfix",
    "Colon",
    "Function",
    "AddTo",
    "DivideBy",
    "SubtractFrom",
    "TimesBy",
    "ReplaceAll",
    "ReplaceRepeated",
    "RuleDelayed",
    "Rule",
    "Condition",
    "StringExpression",
    "Optional",
    "Alternatives",
    "Repeated",
    "RepeatedNull",
    "SuchThat",
    "DoubleLeftTee",
    "DoubleRightTee",
    "DownTee",
    "LeftTee",
    "Perpendicular",  # 190
    "RightTee",  # 190
    # In WMA, `RoundImplies` has a
    # larger precedence value (240) than Not (230),
    # but behaves as it has a precedence
    # between RightTee and UpTee, both with
    # a precedence value of 190.
    #
    # This behavior is not the one in Mathics. For example,
    # the input
    # a\[RoundImplies]b\[UpTee]c//FullForm
    # Is parsed in WMA as
    # RoundImplies[a,UpTee[b,c]],
    # But in Mathics as
    # UpTee[RoundImplies[a, b], c]
    #    "RoundImplies", # WMA->240, Mathics->200, Must be ~193
    "UpTee",  # 190   Must be ~197
    "Implies",  # 200
    "Equivalent",
    "Nor",
    "Or",
    "Xor",
    "And",
    "Nand",
    "Not",
    "NotReverseElement",
    "NotSquareSubsetEqual",
    "NotSquareSupersetEqual",
    "NotSubset",
    "NotSubsetEqual",
    "NotSuperset",
    "NotSupersetEqual",
    "ReverseElement",
    "SquareSubset",
    "SquareSubsetEqual",
    "SquareSuperset",
    "SquareSupersetEqual",
    "Subset",
    "SubsetEqual",
    "Superset",
    "SupersetEqual",
    "DoubleLeftArrow",
    "DoubleLeftRightArrow",
    "DoubleRightArrow",
    "DownLeftRightVector",
    "DownLeftTeeVector",
    "DownLeftVector",
    "DownLeftVectorBar",
    "DownRightTeeVector",
    "DownRightVector",
    "DownRightVectorBar",
    "LeftArrow",
    "LeftArrowBar",
    "LeftArrowRightArrow",
    "LeftRightArrow",
    "LeftRightVector",
    "LeftTeeArrow",
    "LeftTeeVector",
    "LeftVector",
    "LeftVectorBar",
    "LowerLeftArrow",
    "LowerRightArrow",
    "RightArrow",
    "RightArrowBar",
    "RightArrowLeftArrow",
    "RightTeeArrow",
    "RightTeeVector",
    "RightVector",
    "RightVectorBar",
    "ShortLeftArrow",
    "ShortRightArrow",
    "UpperLeftArrow",
    "UpperRightArrow",
    "DoubleVerticalBar",
    "NotDoubleVerticalBar",
    "VerticalBar",
    "Equal",
    "Greater",
    "GreaterEqual",
    "Less",
    "LessEqual",
    "GreaterSlantEqual",
    "LessSlantEqual",
    "SameQ",
    "Unequal",
    "UnsameQ",
    "Congruent",
    "CupCap",
    "DotEqual",
    "EqualTilde",
    "Equilibrium",
    "GreaterEqualLess",
    "GreaterFullEqual",
    "GreaterGreater",
    "GreaterLess",
    "GreaterTilde",
    "HumpDownHump",
    "HumpEqual",
    "LeftTriangle",
    "LeftTriangleBar",
    "LeftTriangleEqual",
    "LessEqualGreater",
    "LessFullEqual",
    "LessGreater",
    "LessLess",
    "LessTilde",
    "NestedGreaterGreater",
    "NestedLessLess",
    "NotCongruent",
    "NotCupCap",
    "NotGreater",
    "NotGreaterEqual",
    "NotGreaterFullEqual",
    "NotGreaterLess",
    "NotGreaterTilde",
    "NotLeftTriangle",
    "NotLeftTriangleEqual",
    "NotLess",
    "NotLessEqual",
    "NotLessFullEqual",
    "NotLessGreater",
    "NotLessTilde",
    "NotPrecedes",
    "NotPrecedesSlantEqual",
    "NotPrecedesTilde",
    "NotRightTriangle",
    "NotRightTriangleEqual",
    "NotSucceeds",
    "NotSucceedsSlantEqual",
    "NotSucceedsTilde",
    "NotTilde",
    "NotTildeEqual",
    "NotTildeFullEqual",
    "NotTildeTilde",
    "Precedes",
    "PrecedesEqual",
    "PrecedesSlantEqual",
    "PrecedesTilde",
    "Proportion",
    "Proportional",
    "ReverseEquilibrium",
    "RightTriangle",
    "RightTriangleBar",
    "RightTriangleEqual",
    "Succeeds",
    "SucceedsEqual",
    "SucceedsSlantEqual",
    "SucceedsTilde",
    "Tilde",
    "TildeEqual",
    "TildeFullEqual",
    "TildeTilde",
    # In Mathics, the precedence of these operators is quite low.
    #    "DirectedEdge",  # Mathics 128 , WMA 295
    #    "UndirectedEdge", # Mathics 120, WMA 295
    "SquareUnion",
    "UnionPlus",
    "Span",
    "SquareIntersection",
    "MinusPlus",
    "PlusMinus",
    "Plus",
    "Subtract",  #  310
    #    "Integrate", # In Mathics, this has the default precedence. In WMA, 325
    "CircleMinus",  # 330
    "CirclePlus",
    "Cup",
    "Cap",
    "Coproduct",
    "VerticalTilde",
    "Star",
    "Times",
    "CenterDot",
    "CircleTimes",
    "Vee",
    "Wedge",
    "Diamond",
    "Backslash",
    "Divide",
    "Minus",
    "Dot",
    "CircleDot",
    "SmallCircle",
    "Square",  # 540
    "Del",  # In WMA, has the same precedence as DifferentialD and CapitalDifferentialD
    "CapitalDifferentialD",  # Mathics 560, WMA 550
    "DifferentialD",  # Mathics 560, WMA, 550
    "DoubleDownArrow",  # 580
    "DoubleLongLeftArrow",
    "DoubleLongLeftRightArrow",
    "DoubleLongRightArrow",
    "DoubleUpArrow",
    "DoubleUpDownArrow",
    "DownArrow",
    "DownArrowBar",
    "DownArrowUpArrow",
    "DownTeeArrow",
    "LeftDownTeeVector",
    "LeftDownVector",
    "LeftDownVectorBar",
    "LeftUpDownVector",
    "LeftUpTeeVector",
    "LeftUpVector",
    "LeftUpVectorBar",
    "LongLeftArrow",
    "LongLeftRightArrow",
    "LongRightArrow",
    "ReverseUpEquilibrium",
    "RightDownTeeVector",
    "RightDownVector",
    "RightDownVectorBar",
    "RightUpDownVector",
    "RightUpTeeVector",
    "RightUpVector",
    "RightUpVectorBar",
    "ShortDownArrow",
    "ShortUpArrow",
    "UpArrow",
    "UpArrowBar",
    "UpArrowDownArrow",
    "UpDownArrow",
    "UpEquilibrium",
    "UpTeeArrow",
    "Power",
    "StringJoin",
    "Factorial",
    "Factorial2",
    "Apply",
    "Map",
    "MapApply",  # In WMA, the default precedence (670) is reported
    "Prefix",
    "Decrement",
    "Increment",
    "PreDecrement",
    "PreIncrement",
    "Unset",
    "Derivative",
    "PatternTest",
    "Get",
    "MessageName",
    "Information",
]


@pytest.mark.skipif(MATHICS_NOT_INSTALLED, reason="Requires Mathics-core installed")
@pytest.mark.parametrize(
    (
        "symbol",
        "prec",
    ),
    list(WMA_PRECEDENCES.items()),
)
@pytest.mark.xfail
def test_precedence_values(symbol, prec):
    """

    TrueRelPrecedence[op1_, op2_] :=
             Module[{formatted =
                     ToString[
               HoldForm[ope2[ope1[a, b], c]] /. {ope1 -> op1, ope2 -> op2},
               InputForm]},
                Not[Or[StringPart[formatted, 1] == "(",
                StringPart[formatted, -1] == ")"]]]

    Transpose[{a, ALLOPS}] // TableForm"""

    mathics_prec = session.evaluate(f"Precedence[{symbol}]").value
    print("Check", f"Precedence[{symbol}]=={prec}")
    check_evaluation(
        f"Precedence[{symbol}]=={prec}",
        "True",
        to_string_expr=True,
        to_string_expected=True,
        hold_expected=True,
        failure_message=f"Precendece of {symbol} in mathics {mathics_prec} !=  WMA value {prec}",
        expected_messages=None,
    )


@pytest.mark.skipif(MATHICS_NOT_INSTALLED, reason="Requires Mathics-core installed")
def test_precedence_order():
    """
    Test the precedence order.
    This is a slighly flexible test, which does not
    requires the numerical coincidence of the Precedence values
    with WMA, but just to preserve the order.
    """
    precedence_values = [
        session.evaluate(f"Precedence[{symbol}]").value
        for symbol in SORTED_SYMBOLS_BY_PRECEDENCE
    ]
    fails = []
    for i in range(len(precedence_values) - 1):
        if precedence_values[i] > precedence_values[i + 1]:
            fails.append(
                f"Precedence[{SORTED_SYMBOLS_BY_PRECEDENCE[i]}]={precedence_values[i]}>"
                f"{precedence_values[i+1]}=Precedence[{SORTED_SYMBOLS_BY_PRECEDENCE[i+1]}]"
            )
    for fail in fails:
        print(fail)
    assert len(fails) == 0
