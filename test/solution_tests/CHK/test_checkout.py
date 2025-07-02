from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution().checkout(skus="ABCD") == 115
        assert CheckoutSolution().checkout(skus="AAAAD") == 195
        assert CheckoutSolution().checkout(skus="AAAADG") == -1
        assert CheckoutSolution().checkout(skus="B") == 30
        assert CheckoutSolution().checkout(skus="BB") == 45
        assert CheckoutSolution().checkout(skus="AAAAAAAAA") == 380
        assert CheckoutSolution().checkout(skus="AEEBBB") == 175
        assert CheckoutSolution().checkout(skus="E") == 40
        assert CheckoutSolution().checkout(skus="EE") == 80
        assert CheckoutSolution().checkout(skus="ABCDE") == 155
        assert CheckoutSolution().checkout(skus="FF") == 20
        assert CheckoutSolution().checkout(skus="FF") == 20
        assert CheckoutSolution().checkout(skus="FFF") == 20
        assert CheckoutSolution().checkout(skus="FFFFFFF") == 50



