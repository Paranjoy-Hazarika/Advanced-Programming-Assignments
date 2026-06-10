import java.util.*;
import java.util.stream.*;

class Student {

    private int id;
    private String name;
    private List<String> courses;
    private Map<String, Integer> scores;

    public Student(int id, String name, List<String> courses, Map<String, Integer> scores) {
        this.id = id;
        this.name = name;
        this.courses = courses;
        this.scores = scores;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<String> getCourses() {
        return courses;
    }

    public Map<String, Integer> getScores() {
        return scores;
    }

    public double getAverageScore() {
        return courses.stream()
                .mapToInt(course -> scores.getOrDefault(course, 0))
                .average()
                .orElse(0.0);
    }
}

class StudentPerformanceAnalyzer {

    public static List<Student> getTopNStudents(List<Student> students, int n) {

        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }

    public static Map<String, Double> getAverageScorePerCourse(List<Student> students) {

        Map<String, List<Integer>> courseScores = new HashMap<>();

        for (Student s : students) {
            for (String course : s.getCourses()) {

                int score = s.getScores().getOrDefault(course, 0);

                courseScores
                        .computeIfAbsent(course, k -> new ArrayList<>())
                        .add(score);
            }
        }

        Map<String, Double> courseAverages = new HashMap<>();

        courseScores.forEach((course, scores) -> {
            double avg = scores.stream()
                    .mapToInt(Integer::intValue)
                    .average()
                    .orElse(0.0);

            courseAverages.put(course, avg);
        });

        return courseAverages;
    }

    public static Set<String> getAllUniqueCourses(List<Student> students) {

        return students.stream()
                .flatMap(student -> student.getCourses().stream())
                .collect(Collectors.toCollection(HashSet::new));
    }
}

public class StudentPerformance {

    public static void main(String[] args) {

        long startTime = System.nanoTime();
    
        List<Student> students = new ArrayList<>();
        Random rand = new Random();
    
        List<String> allCourses = Arrays.asList("Math", "Physics", "Chemistry", "Biology", "CS");
    
        for (int i = 1; i <= 50; i++) {
    
            Map<String, Integer> scores = new HashMap<>();
            List<String> courses = new ArrayList<>();
    
            Collections.shuffle(allCourses);
    
            for (int j = 0; j < 3; j++) {
                String course = allCourses.get(j);
                courses.add(course);
                scores.put(course, rand.nextInt(41) + 60);
            }
    
            students.add(new Student(
                    i,
                    "Student " + i,
                    courses,
                    scores));
        }
    
        List<Student> topStudents =
                StudentPerformanceAnalyzer.getTopNStudents(students, 5);
    
        System.out.println("Top Students:");
        topStudents.forEach(s ->
                System.out.println(s.getName() + " Avg: " + s.getAverageScore()));
    
        Map<String, Double> averages =
                StudentPerformanceAnalyzer.getAverageScorePerCourse(students);
    
        System.out.println("\nCourse Averages:");
        averages.forEach((course, avg) ->
                System.out.println(course + " -> " + avg));
    
        Set<String> courses =
                StudentPerformanceAnalyzer.getAllUniqueCourses(students);
    
        System.out.println("\nUnique Courses:");
        courses.forEach(System.out::println);
    
        long endTime = System.nanoTime();
        System.out.println("\nExecution Time: " + (endTime - startTime) + " ns");
    }
}