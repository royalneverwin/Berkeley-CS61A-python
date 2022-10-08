(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (func p idx)
      (if (eq? p nil)
        nil
        (cons (cons idx (cons (car p) nil)) (func (cdr p) (+ idx 1)))
        )
    )
  (func s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((eq? list1 nil) list2)
        ((eq? list2 nil) list1)
        (else (cond ((inorder? (car list1) (car list2)) (cons (car list1) (merge inorder? (cdr list1) list2)))
                    (else (cons (car list2) (merge inorder? list1 (cdr list2)))
                        )
                )
            )
      )
 
  )
  ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; implement len function
(define (len pair)
    (if (eq? pair nil) 0
          (+ 1 (len (cdr pair)))
          )
    )

;; implement zip function
(define (reverse pair res)
    (if (eq? pair nil) res
        (begin (define res (cons (car pair) res))
               (reverse (cdr pair) res)
            )
        )
    )

(define (zip pairs res)
    (if (eq? pairs nil) (cons (reverse (car res) nil) (cons (reverse (cadr res) nil) nil))
        (if (eq? (len (car pairs)) 2) 
            (begin 
                   (if (eq? res nil) (define res (cons (cons (caar pairs) nil) (cons (cdar pairs) nil)))
                        (define res (cons (cons (caar pairs) (car res)) (cons (cons (car (cdar pairs)) (cadr res)) nil)))
                    ) 
                   (zip (cdr pairs) res)
                   )
            )
        )
    )
;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         expr
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           (define zip_res (zip values nil))
           (define names (car zip_res))
           (define formats (cadr zip_res))
          (cons (list 'lambda names (car (map let-to-lambda body))) (map let-to-lambda formats))
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         (let ((form (car expr))
               (body (cdr expr)))
           (cons form (map let-to-lambda body))
            )
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21