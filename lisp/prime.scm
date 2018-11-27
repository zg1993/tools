(load "utils.scm")


(define (divides? a b)
  (= (remainder a b) 0))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
	((divides? n test-divisor) test-divisor)
	(else (find-divisor n (+ test-divisor 1)))))

(define (prime? n)
  (= (find-divisor n 2) n))



