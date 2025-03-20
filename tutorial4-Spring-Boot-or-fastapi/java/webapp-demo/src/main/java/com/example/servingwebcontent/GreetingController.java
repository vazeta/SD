package com.example.servingwebcontent;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.annotation.Resource;
import javax.servlet.http.HttpSession;

import com.example.servingwebcontent.beans.Number;
import com.example.servingwebcontent.forms.Project;
import com.example.servingwebcontent.thedata.Employee;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Scope;
import org.springframework.context.annotation.ScopedProxyMode;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

@Controller
public class GreetingController {
    @Resource(name = "requestScopedNumberGenerator")
    private Number nRequest;

    @Resource(name = "sessionScopedNumberGenerator")
    private Number nSession;

    @Resource(name = "applicationScopedNumberGenerator")
    private Number nApplication;

    @Bean
    @Scope(value = WebApplicationContext.SCOPE_REQUEST, proxyMode = ScopedProxyMode.TARGET_CLASS)
    public Number requestScopedNumberGenerator() {
        return new Number();
    }

    @Bean
    @Scope(value = WebApplicationContext.SCOPE_SESSION, proxyMode = ScopedProxyMode.TARGET_CLASS)
    public Number sessionScopedNumberGenerator() {
        return new Number();
    }

    @Bean
    @Scope(value = WebApplicationContext.SCOPE_APPLICATION, proxyMode = ScopedProxyMode.TARGET_CLASS)
    public Number applicationScopedNumberGenerator() {
        return new Number();
    }

    @GetMapping("/")
    public String redirect() {
        return "redirect:/greeting";
    }

	@GetMapping("/greeting")
	public String greeting(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
		model.addAttribute("name", name);
		model.addAttribute("othername", "SD");
		return "greeting";
	}

    @GetMapping("/givemeatable")
	public String atable(Model model) {
        Employee [] theEmployees = { new Employee(1, "José", "9199999", 1890), new Employee(2, "Marisa", "9488444", 2120), new Employee(3, "Hélio", "93434444", 2500)};
        List<Employee> le = new ArrayList<>();
        Collections.addAll(le, theEmployees);
        model.addAttribute("emp", le);
		return "table";
	}

    // from https://attacomsian.com/blog/spring-boot-thymeleaf-form-handling and https://github.com/attacomsian/code-examples
	@GetMapping("/create-project")
    public String createProjectForm(Model model) {
        
        model.addAttribute("project", new Project());
        return "create-project";
    }

    @PostMapping("/save-project")
    public String saveProjectSubmission(@ModelAttribute Project project) {

        // TODO: save project in DB here

        return "result";
    }

    @GetMapping("/counters")
	public String counters(Model model) {
        ServletRequestAttributes attr = (ServletRequestAttributes) RequestContextHolder.currentRequestAttributes();
        HttpSession session = attr.getRequest().getSession(true);
        Integer counter = (Integer) session.getAttribute("counter");
        int c;
        if (counter == null)
            c = 1;
        else
            c = counter + 1;
        session.setAttribute("counter", c);
		model.addAttribute("sessioncounter", c);
		model.addAttribute("requestcounter2", this.nRequest.next());
		model.addAttribute("sessioncounter2", this.nSession.next());
		model.addAttribute("applicationcounter2", this.nApplication.next());
		return "counter";
	}

}