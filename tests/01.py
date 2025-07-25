test = {
  'name': 'Question 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(4, 6, 1))
          8a27d52d885dfcd62a4a92cbfe64d30a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(3, make_test_dice(4, 6, 1))
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(4, make_test_dice(2, 2, 3))
          e9a3dddaa9988fe42dd39d1e2cb3390f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = roll_dice(4, make_test_dice(1, 2, 3))
          >>> a # check that the value is being returned, not printed
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> counted_dice = make_test_dice(4, 1, 2, 6)
          >>> roll_dice(3, counted_dice)
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          >>> # Make sure you call dice exactly num_rolls times!
          >>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
          >>> # Note that a return statement within a loop ends the loop
          >>> roll_dice(1, counted_dice)
          3086e969d799e68cd8468df232597f2c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(9, make_test_dice(6))
          61111a83971d8f9ba02faedcd8b1b63b
          # locked
          >>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> roll_dice(5, make_test_dice(4, 2, 3, 3, 4, 1))
          16
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> roll_dice(2, make_test_dice(1))
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 3, 2, 1)
          >>> roll_dice(1, dice)    # Roll 1 (5)
          5
          >>> roll_dice(4, dice)    # Reset (4, 3, 2, 1)
          1
          >>> roll_dice(2, dice)    # Roll 2 (5, 4)
          9
          >>> roll_dice(3, dice)    # Reset (3, 2, 1)
          1
          >>> roll_dice(3, dice)    # Roll 3 (5, 4, 3)
          12
          >>> roll_dice(2, dice)    # Reset (2, 1)
          1
          >>> roll_dice(4, dice)    # Roll 4 (5, 4, 3, 2)
          14
          >>> roll_dice(1, dice)    # Reset (1)
          1
          >>> roll_dice(5, dice)    # Roll 5 (5, 4, 3, 2, 1)
          1
          >>> roll_dice(10, dice)    # Roll 10 (5, 4, 3, 2, 1, 5, 4, 3, 2, 1)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> dice = make_test_dice(2, 4, 3, 5, 2, 2)
          >>> roll_dice(4, dice)
          14
          >>> roll_dice(4, dice)
          10
          >>> roll_dice(3, dice)
          10
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 4, 5, 4, 3)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(1, dice)
          5
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(3, dice)
          12
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 2)
          >>> roll_dice(4, dice)
          14
          >>> roll_dice(3, dice)
          12
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 4, 1, 3, 4)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(2, dice)
          7
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(1, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4,)
          >>> roll_dice(4, dice)
          16
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 3, 5)
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(5, dice)
          18
          >>> roll_dice(3, dice)
          10
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 5, 4)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(1, dice)
          4
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2,)
          >>> roll_dice(4, dice)
          8
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 3)
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 5)
          >>> roll_dice(4, dice)
          18
          >>> roll_dice(2, dice)
          9
          >>> roll_dice(5, dice)
          22
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 4)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 1, 3, 5)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(1, dice)
          5
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 2, 1, 2, 3, 2)
          >>> roll_dice(2, dice)
          5
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 5, 1, 3)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 1, 4)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4, 5)
          >>> roll_dice(2, dice)
          9
          >>> roll_dice(4, dice)
          18
          >>> roll_dice(5, dice)
          22
          >>> roll_dice(3, dice)
          14
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 5, 1, 4, 3)
          >>> roll_dice(1, dice)
          3
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 1, 5, 2, 5, 3)
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(4, dice)
          13
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2,)
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(4, dice)
          8
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 3)
          >>> roll_dice(4, dice)
          10
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 3, 5, 5, 1, 2)
          >>> roll_dice(3, dice)
          11
          >>> roll_dice(3, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3,)
          >>> roll_dice(4, dice)
          12
          >>> roll_dice(1, dice)
          3
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 1, 3)
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 3, 2, 1)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(3, dice)
          10
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 2, 2)
          >>> roll_dice(3, dice)
          7
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(3, dice)
          7
          >>> roll_dice(5, dice)
          11
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3, 1, 5, 3, 3)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(2, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 4)
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 2, 2, 3, 2, 5)
          >>> roll_dice(3, dice)
          9
          >>> roll_dice(3, dice)
          10
          >>> roll_dice(5, dice)
          14
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 2, 4)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 3)
          >>> roll_dice(3, dice)
          13
          >>> roll_dice(1, dice)
          3
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 3)
          >>> roll_dice(2, dice)
          6
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(1, dice)
          3
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 1, 3)
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 2)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 3, 4, 1, 2)
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(1, dice)
          2
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3,)
          >>> roll_dice(3, dice)
          9
          >>> roll_dice(4, dice)
          12
          >>> roll_dice(4, dice)
          12
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(2, 5, 3, 3)
          >>> roll_dice(1, dice)
          2
          >>> roll_dice(2, dice)
          8
          >>> roll_dice(4, dice)
          13
          >>> roll_dice(2, dice)
          5
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3,)
          >>> roll_dice(2, dice)
          6
          >>> roll_dice(2, dice)
          6
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3, 5, 4, 3)
          >>> roll_dice(3, dice)
          1
          >>> roll_dice(1, dice)
          4
          >>> roll_dice(4, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 4, 5, 1, 4, 5)
          >>> roll_dice(2, dice)
          9
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(4,)
          >>> roll_dice(2, dice)
          8
          >>> roll_dice(3, dice)
          12
          >>> roll_dice(1, dice)
          4
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1,)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(1, dice)
          1
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 1, 5, 5, 5)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(1, dice)
          5
          >>> roll_dice(1, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5, 5, 2, 2, 1, 3)
          >>> roll_dice(2, dice)
          10
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(2, dice)
          7
          >>> roll_dice(2, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(5,)
          >>> roll_dice(4, dice)
          20
          >>> roll_dice(4, dice)
          20
          >>> roll_dice(5, dice)
          25
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 2, 2, 5, 4)
          >>> roll_dice(4, dice)
          1
          >>> roll_dice(5, dice)
          1
          >>> roll_dice(1, dice)
          4
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(1, 3)
          >>> roll_dice(5, dice)
          1
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> dice = make_test_dice(3, 3)
          >>> roll_dice(1, dice)
          3
          >>> roll_dice(4, dice)
          12
          >>> roll_dice(5, dice)
          15
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # generated case
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
