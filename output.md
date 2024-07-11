#### How to create your own (simplistic) implementation of an observable?

Let us implement a simple implementation of an [Observable](https://rxjs.dev/guide/observable) to help us understand the concept a bit more. This isn't a fully fledged Observable, but it is a good starting point.

First let us implement the interfaces (because we are writing our implementations in TypeScript):

```typescript
interface Observer<T> {
  next: (value: T) => void;
  error: (err: any) => void;
  complete: () => void;
}

interface Subscription {
  unsubscribe: () => void;
}

interface SafeObserver<T> extends Observer<T> {
  isUnsubscribed: boolean;
}
```

`Observer` is an object that receives notifications from the observable. Observer has three methods `next`, `error` and `complete`. In order to emit values from the observable, we would just need to call the `next` method, an close it up with `complete`. We would then provide the `Observer` object to the observable function.

Next, let us implement the `Observable` class:

```typescript
class Observable<T> {
  private subscribeFunction: (observer: Observer<T>) => void;

  constructor(subscribeFunction: (observer: Observer<T>) => void) {
    this.subscribeFunction = subscribeFunction;
  }

  subscribe(observer: Observer<T>): Subscription {
    const safeObserver = this.createSafeObserver(observer);
    this.subscribeFunction(safeObserver);

    return {
      unsubscribe: () => {
        safeObserver.isUnsubscribed = true;
      },
    };
  }

  private createSafeObserver(observer: Observer<T>): Observer<T> {
    const safeObserver = {
      next: (value: T) => {
        if (!safeObserver.isUnsubscribed && observer.next) {
          observer.next(value);
        }
      },
      error: (err: any) => {
        if (!safeObserver.isUnsubscribed && observer.error) {
          observer.error(err);
        }
        safeObserver.isUnsubscribed = true;
      },
      complete: () => {
        if (!safeObserver.isUnsubscribed && observer.complete) {
          observer.complete();
        }
        safeObserver.isUnsubscribed = true;
      },
      isUnsubscribed: false,
    };

    return safeObserver;
  }
}
```

And lastly let us end with the use case of the Observable:

```typescript
const myObservable = new Observable<number>((observer) => {
  let count = 0;
  const intervalId = setInterval(() => {
    observer.next(count++);

    if (count > 5) {
      observer.complete();
      clearInterval(intervalId);
    }
  }, 1000);

  return () => {
    clearInterval(intervalId);
  };
});

const myObserver: Observer<number> = {
  next: (value) => console.log("Value:", value),
  error: (err) => console.error("Error:", err),
  complete: () => console.log("Completed"),
};

const subscription = myObservable.subscribe(myObserver);

setTimeout(() => {
  subscription.unsubscribe();
  console.log("Unsubscribed");
}, 7000);
```

A great resource that helped me grasping the concepts of observables is [this one](https://www.youtube.com/watch?v=m40cF91F8_A&ab_channel=AngularNYC).

#### What is the router outlet?

Router outlet is a directive which acts as a placeholder where the Angular Router should insert the component that matches the current route. It is one part of Angular's routing mechanism. The directive is placed inside the template of the component.

```html
<!-- some HTML -->
<router-outlet></router-outlet>
<!-- some HTML -->
```

#### How are routes configured?

Angular Routes are usually defined in a configuration object, typically inside a routing module. Each individual route matches an URL path to a component.

```typescript
// app-routing.module.ts
import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { HomeComponent } from "./home/home.component";
import { AboutComponent } from "./about/about.component";

const routes: Routes = [
  { path: "home", component: HomeComponent },
  { path: "about", component: AboutComponent },
  { path: "", redirectTo: "/home", pathMatch: "full" },
  { path: "**", component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
```

In order to define routes in Angular, we need to import the `RouterModule` and provide them the list of routes. `RouterModule` is used to configure and manage navigation and routing, and additionally it provides services and directives for managing application states and views.

#### What is the forRoot(routes) doing?

`Router.forRoot(routes)` is part of route configuration. The method `forRoot` is used specifically to define top-level routes, if we wanted to define child routes in feature modules, we would use `RouterModule.forChild(routes)`.
