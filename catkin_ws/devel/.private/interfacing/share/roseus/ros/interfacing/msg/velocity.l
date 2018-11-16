;; Auto-generated. Do not edit!


(when (boundp 'interfacing::velocity)
  (if (not (find-package "INTERFACING"))
    (make-package "INTERFACING"))
  (shadow 'velocity (find-package "INTERFACING")))
(unless (find-package "INTERFACING::VELOCITY")
  (make-package "INTERFACING::VELOCITY"))

(in-package "ROS")
;;//! \htmlinclude velocity.msg.html


(defclass interfacing::velocity
  :super ros::object
  :slots (_leftwheel _rightwheel ))

(defmethod interfacing::velocity
  (:init
   (&key
    ((:leftwheel __leftwheel) 0)
    ((:rightwheel __rightwheel) 0)
    )
   (send-super :init)
   (setq _leftwheel (round __leftwheel))
   (setq _rightwheel (round __rightwheel))
   self)
  (:leftwheel
   (&optional __leftwheel)
   (if __leftwheel (setq _leftwheel __leftwheel)) _leftwheel)
  (:rightwheel
   (&optional __rightwheel)
   (if __rightwheel (setq _rightwheel __rightwheel)) _rightwheel)
  (:serialization-length
   ()
   (+
    ;; int8 _leftwheel
    1
    ;; int8 _rightwheel
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _leftwheel
       (write-byte _leftwheel s)
     ;; int8 _rightwheel
       (write-byte _rightwheel s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _leftwheel
     (setq _leftwheel (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _leftwheel 127) (setq _leftwheel (- _leftwheel 256)))
   ;; int8 _rightwheel
     (setq _rightwheel (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _rightwheel 127) (setq _rightwheel (- _rightwheel 256)))
   ;;
   self)
  )

(setf (get interfacing::velocity :md5sum-) "050be0bd30e74f253725230b282a1e21")
(setf (get interfacing::velocity :datatype-) "interfacing/velocity")
(setf (get interfacing::velocity :definition-)
      "int8 leftwheel
int8 rightwheel

")



(provide :interfacing/velocity "050be0bd30e74f253725230b282a1e21")


