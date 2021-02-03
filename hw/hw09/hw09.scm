
; Tail recursion

(define (replicate x n)
  (define (f arr curr)
    (if (= curr 0) arr
      (f (append arr `(,x)) (- curr 1))
    )
  )
  (f '() n)
)

(define (accumulate combiner start n term)
  (define (f curr total)
    (if (= curr n) (combiner total (term n))
      (f (+ curr 1) (combiner total (term curr)))
    )
  )
  (f 1 start)
)

(define (accumulate-tail combiner start n term)
  (define (f curr total)
    (if (= curr n) (combiner total (term n))
      (f (+ curr 1) (combiner total (term curr)))
    )
  )
  (f 1 start)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define threes (cons-stream 3 threes))
(define (add s t) (cons-stream (+ (car s) (car t)) (add (cdr-stream s) (cdr-stream t))))
(define multiples-of-three (cons-stream 3 (add multiples-of-three threes)))

(define (list-to-stream lst)
  (if (null? lst) nil
    (cons-stream (car lst) (list-to-stream (cdr lst)))
  )
)

(define (nondecreastream s)
  (define (f buffer arr last lst count)
    (cond ((or (null? arr) (= count 100))
        (append lst `(,buffer)))
      ((or (< last (car arr)) (= last (car arr)))
        (f (append buffer `(,(car arr))) (cdr-stream arr) (car arr) lst (+ count 1))
      )
      (else
        (f `(,(car arr)) (cdr-stream arr) (car arr) (append lst `(,buffer)) (+ count 1))
      )
    )
  )
  (list-to-stream (f '() s -1 '() 0))
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))