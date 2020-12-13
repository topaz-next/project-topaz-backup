# Basic Branch/Pull Request Information
If you followed the Server Setup instructions, you've already cloned Topaz's default branch (called `release`). If you want to make changes and contribute to Topaz, here's a quick guide on how to push changes.

**1 - Set up your fork on GitHub if you haven't already.** This is where you'll push changes to then submit a pull request. You can click on [the fork button in the upper-right, above the main `project-topaz/topaz` repository to fork](https://raw.githubusercontent.com/wiki/project-topaz/topaz/images/github-fork.png).

**2 - Make a new branch from your copy of `release` for _any_ changes.** Do NOT make your changes directly on `release`. Even if you _don't_ plan on making Pull Requests, make a new branch for your personal changes - this lets you easily update your copy of Topaz's `release` branch and merge it into your personal branch. **Making changes on `release` will prevent you from making different changes until the Pull Request you've opened is reviewed and incorporated.**

You can make a branch for anything, but typically it's for a unit of work, which could be something as overarching as SQL edits for all mobs, something more project focused like a single BCNM, or fixing a single bug.

Open your preferred Git client, select `release`, and choose "make branch" (your exact process may vary depending on your Git client). Choose a name for the branch. Select this new branch and "checkout" it to switch to that branch.

If you've made any changes at this point, you'll get an error and be forced to "commit" or "stash" your changes. Commit means bundling the changes you have made on your local machine compared against the branch's original state - a "hard" save. Stash is a temporary "soft" save which lets you change branches and restore that work when you come back. 

**3 - In the new, checked out branch, make the changes as needed.** When you've tested and are comfortable with the work, open your Git client and choose to Commit your changes to the branch. In the window that appears, make sure any changes that you don't _intend_ to change on Topaz (ex: customized settings or scripts that you don't want merged into Topaz) are not included in your commit. You can choose to "Push" from here to send the changes from your local copy to your remote repository. 

**4 - In your remote repository, make sure you're on your new branch which you're looking to contribute from and select New Pull Request.** Fill out the relevant checkboxes, put in an appropriate title, etc.

**5 - Upon review and you making any requested changes, your Pull Request will be merged** with Topaz's `release` branch, or a new branch if it's large enough or changed something which warrants further testing before final merge into `release`. All new "side" branches Topaz creates in this manner are merged into Topaz's `canary` branch for ease of testing, or for servers that want to try out cutting-edge features.

**NOTE:** For custom servers, it's probably best to have a separate repository entirely for your server versus your local copy of Topaz's vanilla build. That way you can clone/download/branch/edit/commit for contributions to Topaz without interfering with files in use by your server.

# Keeping Current With Topaz
You'll want to consistently update your local copy of Topaz's `release` branch with recent changes submitted by contributors. This is part of why working on branches when you have WIPs is important. In order to update both your local and remote `release`:
1. Ensure you're on your `release` branch and have no other local branches checked out
2. Choose "Pull" from the menu of whichever Git tool you're using
3. Select the Topaz remote branch to pull in updates from. Remember Topaz's default branch is `release`. If you haven't pulled from Topaz in a while, you'll want to do a "Fetch" first to update the remote listings in your Git tool.
4. Pull from Topaz's remote `release` into your local `release` copy. 
5. You'll now need to update your remote repository using the "Push" command. This updates your remote copy ("origin") to reflect the new updates you just pulled locally.

# Submitting to Multiple Repositories
[You can use git rebase](https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request) to send commits from other locations to topaz in order to submit to multiple locations and/or repoint.

Alternatively, pull a fork of Topaz and copy **changes only** manually. 

