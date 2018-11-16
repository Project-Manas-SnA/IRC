;; Auto-generated. Do not edit!


(when (boundp 'learning_ros::WordCount)
  (if (not (find-package "LEARNING_ROS"))
    (make-package "LEARNING_ROS"))
  (shadow 'WordCount (find-package "LEARNING_ROS")))
(unless (find-package "LEARNING_ROS::WORDCOUNT")
  (make-package "LEARNING_ROS::WORDCOUNT"))
(unless (find-package "LEARNING_ROS::WORDCOUNTREQUEST")
  (make-package "LEARNING_ROS::WORDCOUNTREQUEST"))
(unless (find-package "LEARNING_ROS::WORDCOUNTRESPONSE")
  (make-package "LEARNING_ROS::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass learning_ros::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod learning_ros::WordCountRequest
  (:init
   (&key
    ((:words __words) "")
    )
   (send-super :init)
   (setq _words (string __words))
   self)
  (:words
   (&optional __words)
   (if __words (setq _words __words)) _words)
  (:serialization-length
   ()
   (+
    ;; string _words
    4 (length _words)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _words
       (write-long (length _words) s) (princ _words s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _words
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _words (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass learning_ros::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod learning_ros::WordCountResponse
  (:init
   (&key
    ((:count __count) 0)
    )
   (send-super :init)
   (setq _count (round __count))
   self)
  (:count
   (&optional __count)
   (if __count (setq _count __count)) _count)
  (:serialization-length
   ()
   (+
    ;; int32 _count
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _count
       (write-long _count s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _count
     (setq _count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass learning_ros::WordCount
  :super ros::object
  :slots ())

(setf (get learning_ros::WordCount :md5sum-) "4dd4fc0aa84b04c0886a72138fb27c19")
(setf (get learning_ros::WordCount :datatype-) "learning_ros/WordCount")
(setf (get learning_ros::WordCount :request) learning_ros::WordCountRequest)
(setf (get learning_ros::WordCount :response) learning_ros::WordCountResponse)

(defmethod learning_ros::WordCountRequest
  (:response () (instance learning_ros::WordCountResponse :init)))

(setf (get learning_ros::WordCountRequest :md5sum-) "4dd4fc0aa84b04c0886a72138fb27c19")
(setf (get learning_ros::WordCountRequest :datatype-) "learning_ros/WordCountRequest")
(setf (get learning_ros::WordCountRequest :definition-)
      "string words
---
int32 count

")

(setf (get learning_ros::WordCountResponse :md5sum-) "4dd4fc0aa84b04c0886a72138fb27c19")
(setf (get learning_ros::WordCountResponse :datatype-) "learning_ros/WordCountResponse")
(setf (get learning_ros::WordCountResponse :definition-)
      "string words
---
int32 count

")



(provide :learning_ros/WordCount "4dd4fc0aa84b04c0886a72138fb27c19")


