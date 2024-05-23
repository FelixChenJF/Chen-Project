document.addEventListener('DOMContentLoaded', function() {
    const courseNames = document.querySelectorAll('.course-name');
    const courseDetails = document.querySelectorAll('.course-detail');

    courseNames.forEach(courseName => {
        courseName.addEventListener('click', function() {
            const courseId = this.getAttribute('data-course-id');

            // Hide all course details
            courseDetails.forEach(detail => {
                detail.style.display = 'none';
            });

            // Show the selected course detail
            const selectedCourse = document.getElementById(`course-${courseId}`);
            if (selectedCourse) {
                selectedCourse.style.display = 'block';
            }
        });
    });
});
