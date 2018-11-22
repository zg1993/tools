(define (count-change amount)
  (cc amount 5))

(define (cc amount kind)
  (cond ((= amount 0) 1)
	((or (< amount 0) (= kind 0)) 0)
	(else (+ (cc amount (- kind 1)) (cc (remain amount kind) kind)))))

(define (remain amount kind)
  (cond ((= kind 5) (- amount 10))
	((= kind 4) (- amount 50))
	((= kind 3) (- amount 1))
	((= kind 2) (- amount 25))
	((= kind 1) (- amount 5))))

(define (num x)
  (let ((g (- x 1)))
    (let ((y (- g 1)))
      y)))


