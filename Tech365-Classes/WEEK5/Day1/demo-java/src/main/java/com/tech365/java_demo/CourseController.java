package com.tech365.java_demo;

import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CourseController {

    @GetMapping("/")
    public String home() {
        return "Tech365 Spring Boot API is running";
    }

    @GetMapping("/api/courses")
    public List<Map<String, Object>> courses() {
        return List.of(
            Map.of("id", 1, "name", "Data Analytics"),
            Map.of("id", 2, "name", "DevOps"),
            Map.of("id", 3, "name", "Software Development")
        );
    }
}